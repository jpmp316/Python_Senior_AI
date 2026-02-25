# Sistema de pruebas

Estructura recomendada según pirámide de testing:

- `tests/unit/`: lógica pura sin base de datos ni red. Se usan mocks y monkeypatch.
- `tests/integration/`: integración entre componentes reales (servicios + BD, API + servicios).
- `tests/e2e/`: flujos completos del usuario con cliente HTTP.
- `tests/fixtures/`: fixtures reutilizables y configuración de prueba.
- `tests/factories/`: generadores de datos deterministas para tests.
- `tests/data/`: datos estáticos (JSON/CSV) usados en casos parametrizados.

Ejecución rápida:

```
pytest
```
