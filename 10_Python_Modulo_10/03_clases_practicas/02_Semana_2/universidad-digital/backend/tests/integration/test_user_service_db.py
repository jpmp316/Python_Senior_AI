from __future__ import annotations

import pytest

from app.users.schemas import UserCreate
from app.users.services import create_user, get_user


@pytest.mark.integration
def test_create_user_persists_and_hashes(db_session, seed_roles) -> None:
    # Arrange
    payload = UserCreate(
        email="nuevo@example.com",
        full_name="Nuevo Usuario",
        password="Password123!",
        role_ids=[seed_roles["Estudiante"].id],
    )

    # Act
    user = create_user(db_session, payload)
    found = get_user(db_session, user.id)

    # Assert
    assert found.email == "nuevo@example.com"
    assert found.hashed_password != payload.password
    assert found.roles[0].name == "Estudiante"
