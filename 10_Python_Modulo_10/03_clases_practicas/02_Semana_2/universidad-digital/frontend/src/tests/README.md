# Sistema de pruebas frontend

## Estructura

- `src/tests/setup/`: configuración global de Vitest y matchers.
- `src/tests/unit/`: pruebas de comportamiento del componente aislado.
- `src/tests/interaction/`: pruebas de interacción con `userEvent`.
- `src/tests/functional/`: validación de cambios en UI tras acciones.
- `src/tests/fixtures/`: datos reutilizables y deterministas.

## Principio rector

Mientras más se parezca al uso real del usuario, más confiable es el test.

## Uso de IA como copiloto

Prompts útiles:

- "Sugiere casos límite faltantes para TaskForm y TaskList con enfoque BDD."
- "Revisa estos tests y propón simplificaciones sin perder cobertura."
- "Detecta over-testing o asserts redundantes en estos archivos."
- "Refactoriza duplicación en pruebas de interacción sin perder claridad."
