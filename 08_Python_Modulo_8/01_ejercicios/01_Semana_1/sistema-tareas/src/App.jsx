import { useState } from 'react'
import Navbar from './components/Navbar.jsx'
import TaskForm from './components/TaskForm.jsx'
import TaskList from './components/TaskList.jsx'

const initialTasks = [
  { id: 'task-1', label: 'Comprar pan' },
  { id: 'task-2', label: 'Estudiar React' },
  { id: 'task-3', label: 'Revisar Tailwind CSS' },
]

function App() {
  const [tasks] = useState(initialTasks)
  const [newTask, setNewTask] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault()
  }

  const handleChange = (event) => {
    setNewTask(event.target.value)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-sky-50 to-white">
      <Navbar title="Sistema de Tareas" />
      <main className="mx-auto flex min-h-[calc(100vh-104px)] max-w-4xl flex-col items-center px-4 py-14">
        <section className="w-full text-center">
          <h1 className="text-4xl font-bold tracking-tight text-slate-900">
            Organiza tu día
          </h1>
          <p className="mt-4 text-base text-slate-600">
            Visualiza tus pendientes y prepara el flujo para agregar nuevas tareas en
            próximas iteraciones.
          </p>
        </section>
        <div className="mt-12 flex w-full flex-col items-center gap-12">
          <TaskList tasks={tasks} />
          <TaskForm value={newTask} onChange={handleChange} onSubmit={handleSubmit} />
        </div>
      </main>
    </div>
  )
}

export default App
