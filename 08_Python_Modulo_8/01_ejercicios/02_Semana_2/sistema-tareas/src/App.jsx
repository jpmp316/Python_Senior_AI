import { useEffect, useState } from 'react';
import Footer from './components/Footer.jsx';
import Header from './components/Header.jsx';
import TaskForm from './components/TaskForm.jsx';
import TaskList from './components/TaskList.jsx';

const initialTasks = [
  { id: 'task-1', title: 'Comprar pan', completed: false },
  { id: 'task-2', title: 'Estudiar React', completed: false },
  { id: 'task-3', title: 'Revisar Tailwind CSS', completed: false },
];

/**
 * App.jsx
 * Punto de entrada de la vista que orquesta la lógica y composición del sistema de tareas.
 * @component
 * @returns {JSX.Element}
 */
function App() {
  const [tasks, setTasks] = useState(initialTasks);
  const [newTask, setNewTask] = useState('');

  useEffect(() => {
    const pendingCount = tasks.filter((task) => !task.completed).length;
    document.title = `Tareas pendientes: ${pendingCount}`;
  }, [tasks]);

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  const handleChange = (event) => {
    setNewTask(event.target.value);
  };

  // Se centraliza el toggle para asegurar un único punto de mutación controlada.
  const handleToggleTask = (taskId) => {
    setTasks((previousTasks) =>
      previousTasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task,
      ),
    );
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <Header
        title="Sistema de Tareas"
        subtitle="Organiza tu día y mantén visibilidad de los pendientes prioritarios."
      />
      <main className="mx-auto flex min-h-[calc(100vh-240px)] max-w-5xl flex-col items-center px-4 py-12">
        <section className="w-full max-w-3xl text-center sm:text-left">
          <h2 className="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl">
            Planifica tus entregables
          </h2>
          <p className="mt-4 text-base text-slate-600">
            Visualiza tus pendientes actuales y prepara el flujo para agregar nuevas tareas en
            próximas iteraciones.
          </p>
        </section>
        <div className="mt-12 flex w-full flex-col items-center gap-12">
          <TaskList tasks={tasks} onToggleTask={handleToggleTask} />
          <TaskForm value={newTask} onChange={handleChange} onSubmit={handleSubmit} />
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default App;

/** IA Refactor Summary: Se modularizó la vista principal integrando componentes especializados, se agregó control del estado de tareas y un efecto para reflejar los pendientes activos. */
