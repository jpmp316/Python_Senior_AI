from __future__ import annotations

import json
from pathlib import Path

import pytest
from jose import JWTError

from app.core import security
from app.core.config import settings


@pytest.mark.unit
def test_hash_and_verify_password() -> None:
    password = "Password123!"
    hashed = security.hash_password(password)
    assert hashed != password
    assert security.verify_password(password, hashed) is True
    assert security.verify_password("otra", hashed) is False


@pytest.mark.unit
def test_create_access_token_requires_secret(monkeypatch) -> None:
    monkeypatch.setattr(settings, "jwt_secret", None)
    with pytest.raises(RuntimeError):
        security.create_access_token("1", jti="abc123")


@pytest.mark.unit
def test_decode_access_token_invalid() -> None:
    with pytest.raises(JWTError):
        security.decode_access_token("token-invalido")


@pytest.mark.unit
@pytest.mark.security
@pytest.mark.parametrize(
    "email",
    json.loads(
        (Path(__file__).resolve().parents[1] / "data" / "invalid_payloads.json").read_text(
            encoding="utf-8"
        )
    )["emails"],
)
def test_invalid_emails_are_rejected(email: str) -> None:
    with pytest.raises(Exception):
        from app.users.schemas import UserCreate

        UserCreate(email=email, full_name="Nombre", password="Password123!")
