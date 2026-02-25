from __future__ import annotations

import pytest


@pytest.mark.e2e
@pytest.mark.skip(reason="Módulos de pagos y certificados no implementados aún.")
def test_payment_and_certificate_flow() -> None:
    pass
