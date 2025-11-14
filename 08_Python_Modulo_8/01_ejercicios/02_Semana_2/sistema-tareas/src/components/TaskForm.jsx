import PropTypes from 'prop-types';

/**
 * TaskForm.jsx
 * Formulario controlado para capturar nuevas tareas, manteniendo validaciones básicas.
 * @component
 * @author Cursor AI
 * @param {object} props - Propiedades del componente.
 * @param {string} props.value - Valor actual del campo de texto.
 * @param {function} props.onChange - Manejador de cambios del input.
 * @param {function} props.onSubmit - Acción al enviar el formulario.
 * @returns {JSX.Element}
 */
const TaskForm = ({ value, onChange, onSubmit }) => (
  <section className="w-full max-w-3xl">
    <form
      className="mt-8 flex flex-col gap-4 rounded-3xl border border-slate-200/70 bg-white/80 p-8 shadow-xl shadow-sky-100 backdrop-blur"
      onSubmit={onSubmit}
      noValidate
    >
      <div className="flex flex-col gap-2 sm:flex-row sm:items-center">
        <label className="text-sm font-medium text-slate-600" htmlFor="task">
          Nueva tarea
        </label>
        <input
          id="task"
          name="task"
          type="text"
          className="flex-1 rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-800 shadow-sm transition focus:border-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-200"
          placeholder="Describe tu siguiente pendiente"
          value={value}
          onChange={onChange}
          autoComplete="off"
          aria-describedby="task-helper"
        />
      </div>
      {/* Se mantiene el botón deshabilitado lógicamente para futuras iteraciones */}
      <div className="flex flex-col items-start gap-3 sm:flex-row sm:items-center">
        <p id="task-helper" className="text-xs text-slate-500">
          El formulario se habilitará en la siguiente iteración.
        </p>
        <button
          type="submit"
          className="inline-flex items-center justify-center rounded-full bg-sky-500 px-6 py-2 text-sm font-semibold text-white transition hover:bg-sky-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600"
          disabled
        >
          Agregar tarea
        </button>
      </div>
    </form>
  </section>
);

TaskForm.propTypes = {
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired,
};

export default TaskForm;

/** IA Refactor Summary: Se documentó el formulario, se añadió un comentario de intención y se deshabilitó el botón para reflejar el flujo actual. */
