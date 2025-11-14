import PropTypes from 'prop-types';
import TaskItem from './TaskItem.jsx';

/**
 * TaskList.jsx
 * Contenedor de la lista de tareas que delega la representación individual a TaskItem.
 * @component
 * @author Cursor AI
 * @param {object} props - Propiedades del componente.
 * @param {Array<{id: string, title: string, completed: boolean}>} props.tasks - Colección de tareas a mostrar.
 * @param {function} props.onToggleTask - Callback para alternar el estado de una tarea.
 * @returns {JSX.Element}
 */
const TaskList = ({ tasks, onToggleTask }) => (
  <section className="w-full max-w-3xl">
    <div className="rounded-3xl border border-slate-200/70 bg-white/85 p-8 shadow-xl shadow-sky-100 backdrop-blur">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <h2 className="text-xl font-semibold text-slate-900 sm:text-2xl">Tareas pendientes</h2>
        <span className="text-xs font-medium uppercase tracking-wide text-slate-400 sm:text-sm">
          Lista interactiva
        </span>
      </div>
      {/* Se delega la renderización de cada ítem para mantener el componente acotado */}
      <ul className="mt-6 space-y-3">
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            title={task.title}
            completed={task.completed}
            onToggle={() => onToggleTask(task.id)}
          />
        ))}
      </ul>
    </div>
  </section>
);

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      completed: PropTypes.bool.isRequired,
    }),
  ).isRequired,
  onToggleTask: PropTypes.func.isRequired,
};

export default TaskList;

/** IA Refactor Summary: Se convirtió la lista en un contenedor declarativo que usa TaskItem, tipando props y añadiendo notas responsivas. */
