from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.core.errors import ConflictError, NotFoundError
from app.roles.models import Role
from app.users.schemas import UserCreate
from app.users.services import create_user


def _scalars_result(items: list):
    result = MagicMock()
    result.all.return_value = items
    return result


def _role(name: str):
    return SimpleNamespace(name=name)


@pytest.mark.unit
def test_create_user_assigns_default_role(monkeypatch) -> None:
    # Arrange
    db = MagicMock()
    # Registrar modelos dependientes para relaciones ORM
    from app.enrollments import models as _enrollments  # noqa: F401
    from app.grades import models as _grades  # noqa: F401

    db.scalar.side_effect = [None, Role(name="Estudiante")]
    db.scalars.return_value = _scalars_result([])
    monkeypatch.setattr("app.users.services.hash_password", lambda _: "hashed")
    payload = UserCreate(email="user@example.com", full_name="Usuario", password="Password123!")

    # Act
    user = create_user(db, payload)

    # Assert
    assert user.email == "user@example.com"
    assert user.roles and user.roles[0].name == "Estudiante"
    db.add.assert_called_once()
    db.commit.assert_called_once()


@pytest.mark.unit
def test_create_user_requires_long_password_for_admin(monkeypatch) -> None:
    # Arrange
    db = MagicMock()
    db.scalar.return_value = None
    db.scalars.return_value = _scalars_result([_role("Administrador")])
    monkeypatch.setattr("app.users.services.hash_password", lambda _: "hashed")
    payload = UserCreate(
        email="admin@example.com",
        full_name="Admin",
        password="Short123!",
        role_ids=[1],
    )

    # Act / Assert
    with pytest.raises(ConflictError):
        create_user(db, payload)


@pytest.mark.unit
def test_create_user_invalid_role_ids(monkeypatch) -> None:
    # Arrange
    db = MagicMock()
    db.scalar.return_value = None
    db.scalars.return_value = _scalars_result([_role("Docente")])
    monkeypatch.setattr("app.users.services.hash_password", lambda _: "hashed")
    payload = UserCreate(
        email="docente@example.com",
        full_name="Docente",
        password="Password123!",
        role_ids=[1, 2],
    )

    # Act / Assert
    with pytest.raises(NotFoundError):
        create_user(db, payload)
