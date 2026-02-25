from __future__ import annotations

import pytest

from app.core.errors import ConflictError
from app.enrollments.schemas import EnrollmentCreate
from app.enrollments.services import create_enrollment


@pytest.mark.integration
def test_enrollment_unique_constraint(db_session, student_user, subject, period) -> None:
    # Arrange
    payload = EnrollmentCreate(
        user_id=student_user.id,
        subject_id=subject.id,
        period_id=period.id,
    )

    # Act
    create_enrollment(db_session, payload, student_user)

    # Assert
    with pytest.raises(ConflictError):
        create_enrollment(db_session, payload, student_user)
