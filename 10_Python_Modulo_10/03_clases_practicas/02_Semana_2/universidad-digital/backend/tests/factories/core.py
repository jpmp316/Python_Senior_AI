from __future__ import annotations

from datetime import date, timedelta
from itertools import count

_user_counter = count(1)
_subject_counter = count(1)
_period_counter = count(1)


def user_payload(
    *,
    email: str | None = None,
    full_name: str | None = None,
    password: str | None = None,
    role_ids: list[int] | None = None,
) -> dict:
    idx = next(_user_counter)
    return {
        "email": email or f"estudiante{idx}@example.com",
        "full_name": full_name or f"Estudiante {idx}",
        "password": password or "Password123!",
        "role_ids": role_ids,
    }


def subject_payload(*, code: str | None = None, name: str | None = None, credits: int | None = None) -> dict:
    idx = next(_subject_counter)
    return {
        "code": code or f"MAT{idx:03d}",
        "name": name or f"Materia {idx}",
        "credits": credits if credits is not None else 4,
    }


def period_payload(*, code: str | None = None, name: str | None = None) -> dict:
    idx = next(_period_counter)
    start = date.today()
    end = start + timedelta(days=120)
    return {
        "code": code or f"PER{idx:03d}",
        "name": name or f"Periodo {idx}",
        "start_date": start,
        "end_date": end,
    }


def enrollment_payload(*, user_id: int, subject_id: int, period_id: int) -> dict:
    return {
        "user_id": user_id,
        "subject_id": subject_id,
        "period_id": period_id,
    }
