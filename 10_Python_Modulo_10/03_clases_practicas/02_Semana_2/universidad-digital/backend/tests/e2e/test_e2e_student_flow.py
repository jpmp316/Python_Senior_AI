from __future__ import annotations

import pytest

from app.core.security import hash_password
from app.roles.models import Role
from app.users.models import User


@pytest.mark.e2e
def test_student_flow_registration_login_enrollment(api_client, db_session, seed_roles, subject, period) -> None:
    # Arrange: crear admin en BD para registrar estudiantes
    admin = User(
        email="admin-flow@example.com",
        full_name="Admin Flow",
        hashed_password=hash_password("AdminPassword123!"),
    )
    admin.roles = [seed_roles["Administrador"]]
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)

    # Act: login admin -> crear estudiante (registro controlado)
    admin_login = api_client.post(
        "/auth/login", json={"email": admin.email, "password": "AdminPassword123!"}
    )
    assert admin_login.status_code == 200

    student_payload = {
        "email": "flow-student@example.com",
        "full_name": "Flow Student",
        "password": "StudentPass123!",
        "role_ids": [seed_roles["Estudiante"].id],
    }
    create_student = api_client.post("/users/", json=student_payload)
    assert create_student.status_code == 201
    student_id = create_student.json()["id"]

    # Act: login estudiante -> matriculación
    api_client.post("/auth/login", json={"email": student_payload["email"], "password": student_payload["password"]})
    enroll_payload = {
        "user_id": student_id,
        "subject_id": subject.id,
        "period_id": period.id,
    }
    enroll_response = api_client.post("/enrollments/", json=enroll_payload)

    # Assert
    assert enroll_response.status_code == 201
    assert enroll_response.json()["user_id"] == student_id
