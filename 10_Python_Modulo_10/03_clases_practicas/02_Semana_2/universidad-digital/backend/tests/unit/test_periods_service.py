from __future__ import annotations

from datetime import date
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from app.core.errors import ConflictError
from app.periods.services import create_period


@pytest.mark.unit
def test_create_period_rejects_invalid_dates() -> None:
    # Arrange
    db = MagicMock()
    db.scalar.return_value = None
    payload = SimpleNamespace(
        code="PER001",
        name="Periodo 1",
        start_date=date(2026, 3, 10),
        end_date=date(2026, 2, 10),
    )

    # Act / Assert
    with pytest.raises(ConflictError):
        create_period(db, payload)
