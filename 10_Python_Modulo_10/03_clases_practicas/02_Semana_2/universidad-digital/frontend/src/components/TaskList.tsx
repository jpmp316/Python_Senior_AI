export type TaskItem = {
  id: string;
  title: string;
  completed: boolean;
};

export type TaskListProps = {
  tasks: TaskItem[];
  onToggle: (taskId: string) => void;
  onDelete: (taskId: string) => void;
};

export default function TaskList({ tasks, onToggle, onDelete }: TaskListProps) {
  if (tasks.length === 0) {
    return <p role="status">No hay tareas todavía.</p>;
  }

  return (
    <ul aria-label="Lista de tareas">
      {tasks.map((task) => {
        const inputId = `task-${task.id}`;
        return (
          <li key={task.id}>
            <div>
              <input
                id={inputId}
                type="checkbox"
                checked={task.completed}
                onChange={() => onToggle(task.id)}
              />
              <label htmlFor={inputId}>{task.title}</label>
              <span>{task.completed ? "Completada" : "Pendiente"}</span>
            </div>
            <button type="button" onClick={() => onDelete(task.id)}>
              Eliminar
            </button>
          </li>
        );
      })}
    </ul>
  );
}
