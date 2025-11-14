import PropTypes from 'prop-types'

const TaskList = ({ tasks }) => (
  <section className="w-full max-w-3xl">
    <div className="rounded-3xl border border-slate-200/70 bg-white/80 p-8 shadow-xl shadow-sky-100 backdrop-blur">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold text-slate-900">Tareas pendientes</h2>
        <span className="text-xs font-medium uppercase tracking-wide text-slate-400">
          Lista estática
        </span>
      </div>
      <ul className="mt-6 space-y-3">
        {tasks.map((task) => (
          <li
            key={task.id}
            className="flex items-center justify-between rounded-2xl border border-slate-100 bg-gradient-to-r from-white via-slate-50 to-white px-5 py-3 text-sm font-medium text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:border-slate-200 hover:shadow-md"
          >
            <span>{task.label}</span>
            <span className="text-xs font-semibold uppercase tracking-wide text-slate-400">
              Estática
            </span>
          </li>
        ))}
      </ul>
    </div>
  </section>
)

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
    }),
  ).isRequired,
}

export default TaskList

