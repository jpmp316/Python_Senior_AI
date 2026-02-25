from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.core.errors import ConflictError, NotFoundError
from app.enrollments.schemas import EnrollmentCreate
from app.enrollments.services import create_enrollment


@pytest.mark.unit
def test_create_enrollment_blocks_student_on_other_user() -> None:
    # Arrange
    db = MagicMock()
    actor = SimpleNamespace(
        id=10,
        email="student@uni.test",
        full_name="Estudiante",
        hashed_password="x",
        roles=[SimpleNamespace(name="Estudiante")],
    )
    payload = EnrollmentCreate(user_id=99, subject_id=1, period_id=1)

    # Act / Assert
    with pytest.raises(ConflictError):
        create_enrollment(db, payload, actor)


@pytest.mark.unit
def test_create_enrollment_requires_existing_user() -> None:
    # Arrange
    db = MagicMock()
    actor = SimpleNamespace(
        id=1,
        email="admin@uni.test",
        full_name="Admin",
        hashed_password="x",
        roles=[SimpleNamespace(name="Administrador")],
    )
    payload = EnrollmentCreate(user_id=1, subject_id=1, period_id=1)
    db.get.return_value = None

    # Act / Assert
    with pytest.raises(NotFoundError):
        create_enrollment(db, payload, actor)
