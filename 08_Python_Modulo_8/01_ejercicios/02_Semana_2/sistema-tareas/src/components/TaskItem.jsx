import PropTypes from 'prop-types';

/**
 * TaskItem.jsx
 * Fila reutilizable que representa una tarea dentro del listado principal.
 * @component
 * @author Cursor AI
 * @param {object} props - Propiedades del componente.
 * @param {string} props.title - Nombre identificador de la tarea.
 * @param {boolean} props.completed - Indicador del estado de la tarea.
 * @param {function} props.onToggle - Controlador para alternar el estado de completado.
 * @returns {JSX.Element}
 */
const TaskItem = ({ title, completed, onToggle }) => (
  <li className="flex items-center justify-between rounded-2xl border border-slate-100 bg-white/95 px-5 py-3 text-sm text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:border-sky-200 hover:shadow-md sm:text-base">
    <div className="flex items-center gap-3">
      {/* Indicador visual minimalista para reforzar el estado de la tarea */}
      <span
        className={`inline-flex h-3 w-3 rounded-full ${
          completed ? 'bg-emerald-500' : 'bg-slate-300'
        }`}
        aria-hidden="true"
      />
      <p
        className={`font-medium ${completed ? 'text-slate-400 line-through' : 'text-slate-700'}`}
      >
        {title}
      </p>
    </div>
    <button
      type="button"
      onClick={onToggle}
      className={`rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wide transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 ${
        completed
          ? 'bg-emerald-50 text-emerald-600 focus-visible:outline-emerald-500'
          : 'bg-sky-50 text-sky-600 focus-visible:outline-sky-500'
      }`}
      aria-pressed={completed}
    >
      {completed ? 'Completada' : 'Pendiente'}
    </button>
  </li>
);

TaskItem.propTypes = {
  title: PropTypes.string.isRequired,
  completed: PropTypes.bool.isRequired,
  onToggle: PropTypes.func.isRequired,
};

export default TaskItem;

/** IA Refactor Summary: Se encapsuló la representación de cada tarea con estados visuales, propiedades tipadas y estilos coherentes para su reutilización. */

