from __future__ import annotations

import pytest


@pytest.mark.integration
def test_login_and_me_endpoint(api_client, student_user) -> None:
    # Arrange
    payload = {"email": student_user.email, "password": "StudentPass123!"}

    # Act
    response = api_client.post("/auth/login", json=payload)

    # Assert
    assert response.status_code == 200
    assert "access_token" in response.json()

    me_response = api_client.get("/auth/me")
    assert me_response.status_code == 200
    assert me_response.json()["email"] == student_user.email
