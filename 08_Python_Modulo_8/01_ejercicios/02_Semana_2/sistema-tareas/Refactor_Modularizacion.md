# Refactor del Sistema de Tareas con React 18, Vite 5 y Tailwind CSS v4

## Contexto y objetivos

- **Motivación**: garantizar separación clara entre lógica y presentación, mejorar la reutilización de componentes y documentar cada decisión para facilitar su explicación y mantenimiento.
- **Alcance**: reorganización del árbol `src/`, creación de componentes `Header`, `TaskList`, `TaskItem`, `TaskForm`, `Footer`, y actualización de `App.jsx` para coordinar la interacción entre ellos.
- **Normativas respetadas**: Airbnb JavaScript Style Guide, OWASP Secure Coding Practices, principios de Clean Code (nombres expresivos, funciones cortas, DRY) y uso exclusivo de utilidades Tailwind CSS v4 para estilos responsivos.

## Cambios principales

### 1. `src/App.jsx`

- **Qué se hizo**: Se convirtió en el orquestador del flujo de tareas, importando todos los componentes modularizados (`Header`, `TaskList`, `TaskForm`, `Footer`).
- **Por qué**:
  - Centralizar la lógica de estado (`useState`) y efectos (`useEffect`) evita propagar mutaciones o efectos secundarios en componentes de presentación.
  - Se añadió un `useEffect` que actualiza el `document.title` con el número de tareas pendientes, mejorando la UX sin comprometer seguridad.
- **Cómo ayuda**:
  - Simplifica pruebas unitarias de cada componente, ya que `App` solo coordina acciones.
  - Mantiene un único punto de verdad para las tareas (`tasks`) y el formulario (`newTask`).

### 2. `src/components/Header.jsx`

- **Qué se hizo**: Creación de cabecera reutilizable que recibe `title` y `subtitle`, con prop-types y valores por defecto.
- **Por qué**:
  - Extraer la cabecera del layout permite reutilizarla o sustituirla sin tocar la lógica del resto del sistema.
  - Se documentó con JSDoc y se añadió un resumen de refactor al final del archivo para consolidar la trazabilidad de cambios.
- **Decisiones clave**:
  - Uso de utilidades Tailwind responsivas (`sm`, `lg`) para asegurar legibilidad desde móviles hasta escritorio.
  - Mantener un badge “Panel principal” como recordatorio contextual en pantallas grandes.

### 3. `src/components/TaskList.jsx`

- **Qué se hizo**: Se transformó en un contenedor declarativo que mapea cada tarea a un `TaskItem`.
- **Por qué**:
  - Evitar duplicación de JSX para cada fila; `TaskItem` encapsula la representación y comportamiento.
  - `TaskList` solo se encarga de la estructura (títulos, layout) y delega la lógica de toggle al callback `onToggleTask`.
- **Beneficios**:
  - Permite cambiar la representación de tareas (tarjetas, filas, etc.) sin afectar a `App`.
  - Reduce complejidad ciclomática y prepara al proyecto para listas filtradas o agrupaciones futuras.

### 4. `src/components/TaskItem.jsx`

- **Qué se hizo**: Componente que representa una tarea individual con botón para alternar su estado.
- **Por qué**:
  - Identificar repetición (cada `<li>` del listado) y convertirla en un componente facilita aplicar nuevas reglas (p. ej. acceso desde teclado, estados ARIA) en un solo lugar.
  - Se añadió un indicador visual minimalista (punto de color) que refuerza la percepción de estado sin depender únicamente de texto.
- **Consideraciones de seguridad**:
  - No se usaron atributos inseguros (`dangerouslySetInnerHTML`, `eval`), cumpliendo OWASP.
  - El `button` usa `aria-pressed` para accesibilidad, evitando scripts personalizados.

### 5. `src/components/TaskForm.jsx`

- **Qué se hizo**: Se documentó, se dejó el botón en estado deshabilitado señalando que el flujo se habilitará en futuras iteraciones y se añadió comentario explicativo.
- **Por qué**:
  - Mantener el formulario como componente controlado simplifica validar entradas posteriores.
  - La documentación aclara que el estado actual es un placeholder, evitando confusiones.
- **Aspectos técnicos**:
  - `noValidate` evita mensajes nativos mientras se define la lógica; se complementará con validaciones propias.
  - Tailwind asegura contrastes y espacios consistentes.

### 6. `src/components/Footer.jsx`

- **Qué se hizo**: Pie de página con información institucional y enlace a documentación OWASP.
- **Por qué**:
  - refuerza la autoría y ofrece un recurso educativo ligado a las prácticas de seguridad adoptadas.
  - `rel="noreferrer noopener"` en el enlace previene ataques de tipo reverse tabnabbing.

## Diseño responsivo y estilos

- Se estandarizó el uso de contenedores con `max-w-5xl` y `max-w-3xl` para mantener consistencia visual.
- Breakpoints `sm` y `lg` ajustan tipografías, gaps y disposición (por ejemplo, cabecera pasa de columna a fila en escritorio).
- Tailwind se usó en todas las capas, evitando CSS externo y garantizando coherencia con Vite 5 + React 18.

## Documentación y trazabilidad

- Cada archivo incluye:
  - Cabecera JSDoc con descripción, props y autoría.
  - Comentarios inline para decisiones clave (delegación en `TaskList`, indicador visual en `TaskItem`, etc.).
  - Bloque final `/** IA Refactor Summary: ... */` que explica el impacto del cambio para auditorías rápidas.
- Esta estructura permite a cualquier desarrollador entender no solo qué se hizo, sino **por qué** se hizo.

## Buenas prácticas de seguridad

- Ausencia de `eval`, `innerHTML` y manipulaciones directas del DOM.
- Uso de props tipados con `PropTypes` para prevenir inyecciones accidentales desde componentes externos.
- Enlaces externos con `rel="noreferrer noopener"` según recomendaciones OWASP.

## Impacto en mantenibilidad

- El código ahora sigue una arquitectura de componentes tipo “Smart (App) + Presentational (resto)”.
- Reducimos la complejidad en `App.jsx` y facilitamos la extensión futura (filtros, contador global, persistencia).
- Los componentes creados pueden incorporarse en otras vistas (dashboard, modal, etc.) sin dependencias ocultas.

## Próximos pasos sugeridos

- Implementar validaciones y habilitar el `TaskForm` con almacenamiento persistente (localStorage o API).
- Añadir pruebas unitarias para `TaskItem` y `TaskList` verificando la propagación de eventos `onToggle`.
- Integrar un sistema de diseño (Design Tokens) que permita compartir tipografías, colores y espaciados a través de Tailwind config.

---

**Resumen ejecutivo**: La refactorización modularizó el sistema en componentes especializados, reforzó la documentación técnica, garantizó cumplimiento de estándares de seguridad y estableció bases sólidas para escalar el proyecto sin degradar la mantenibilidad ni la experiencia de usuario.
