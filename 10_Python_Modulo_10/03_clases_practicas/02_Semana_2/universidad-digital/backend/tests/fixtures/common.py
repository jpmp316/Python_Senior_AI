from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.core.database import Base
from app.core.security import hash_password
from app.periods.models import AcademicPeriod
from app.roles.models import Role
from app.roles.services import ensure_default_roles
from app.subjects.models import Subject
from app.users.models import User
from tests.factories.core import enrollment_payload, period_payload, subject_payload, user_payload


@pytest.fixture(scope="session", autouse=True)
def _test_settings() -> None:
    settings.jwt_secret = "test-secret"
    settings.jwt_expiration_minutes = 30
    settings.auto_create_tables = False
    settings.cookie_secure = False


@pytest.fixture(scope="session")
def db_engine():
    base_dir = Path(__file__).resolve().parents[2] / ".test_artifacts" / "db"
    base_dir.mkdir(parents=True, exist_ok=True)
    db_file = base_dir / "test.db"
    engine = create_engine(
        f"sqlite+pysqlite:///{db_file}",
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
    )
    # Importar modelos para registrar metadata
    from app.auth import models as _auth  # noqa: F401
    from app.enrollments import models as _enrollments  # noqa: F401
    from app.grades import models as _grades  # noqa: F401
    from app.periods import models as _periods  # noqa: F401
    from app.roles import models as _roles  # noqa: F401
    from app.subjects import models as _subjects  # noqa: F401
    from app.users import models as _users  # noqa: F401

    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture()
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(bind=connection, autocommit=False, autoflush=False, class_=Session)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture()
def seed_roles(db_session) -> dict[str, Role]:
    ensure_default_roles(db_session)
    roles = db_session.scalars(select(Role)).all()
    return {role.name: role for role in roles}


@pytest.fixture()
def user_valid_data() -> dict:
    return user_payload()


@pytest.fixture()
def user_invalid_data() -> dict:
    return {
        "email": "no-es-email",
        "full_name": "",
        "password": "123",
        "role_ids": None,
    }


@pytest.fixture()
def subject_data() -> dict:
    return subject_payload()


@pytest.fixture()
def period_data() -> dict:
    return period_payload()


@pytest.fixture()
def admin_user(db_session, seed_roles) -> User:
    admin = User(
        email="admin@example.com",
        full_name="Administrador",
        hashed_password=hash_password("AdminPassword123!"),
    )
    admin.roles = [seed_roles["Administrador"]]
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin


@pytest.fixture()
def student_user(db_session, seed_roles) -> User:
    student = User(
        email="student@example.com",
        full_name="Estudiante",
        hashed_password=hash_password("StudentPass123!"),
    )
    student.roles = [seed_roles["Estudiante"]]
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    return student


@pytest.fixture()
def subject(db_session) -> Subject:
    payload = subject_payload()
    entity = Subject(**payload)
    db_session.add(entity)
    db_session.commit()
    db_session.refresh(entity)
    return entity


@pytest.fixture()
def period(db_session) -> AcademicPeriod:
    payload = period_payload()
    entity = AcademicPeriod(**payload)
    db_session.add(entity)
    db_session.commit()
    db_session.refresh(entity)
    return entity


@pytest.fixture()
def enrollment_data(student_user, subject, period) -> dict:
    return enrollment_payload(user_id=student_user.id, subject_id=subject.id, period_id=period.id)


@pytest.fixture()
def api_client(db_session):
    from app.main import app
    from app.core.deps import get_db

    app.router.on_startup.clear()
    app.router.on_shutdown.clear()

    def _get_db():
        yield db_session

    app.dependency_overrides[get_db] = _get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture()
def api_client_admin(db_session, admin_user):
    from app.main import app
    from app.core.deps import get_current_user_dep, get_db

    app.router.on_startup.clear()
    app.router.on_shutdown.clear()

    def _get_db():
        yield db_session

    def _get_current_user():
        return admin_user

    app.dependency_overrides[get_db] = _get_db
    app.dependency_overrides[get_current_user_dep] = _get_current_user
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture()
def fixed_today() -> date:
    return date(2026, 2, 13)
