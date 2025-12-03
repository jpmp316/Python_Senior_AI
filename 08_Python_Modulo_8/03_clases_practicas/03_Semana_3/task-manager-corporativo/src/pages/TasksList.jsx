import { Link, useNavigate } from "react-router-dom";
import { useTasks } from "../hooks/useTasks";
import { api } from "../api/client";

function TasksList() {
  const { tasks, loading, error, reload } = useTasks();
  const navigate = useNavigate();

  const handDelete = async (id) => {
    if (!confirm("¿Esta seguro que desea eliminar esta tarea?")) return;
    await api.delete(`/tasks/${id}`);
    reload();
  };

  const handLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  const getStatusBadge = (status) => {
    const styles = {
      Pendiente: "bg-yellow-100 text-yellow-800",
      "En progreso": "bg-blue-100 text-blue-800",
      Completada: "bg-green-100 text-green-800",
    };

    return (
      <span
        className={`px-2 py-1 rounded-full text-xs font-medium ${
          styles[status] || "bg-gray-100 text-gray-800"
        }`}
      >
        {status}
      </span>
    );
  };

  const getPrioriryBadge = (priority) => {
    const styles = {
      Alta: "bg-red-100 text-red-800",
      Media: "bg-orange-100 text-orange-800",
      Baja: "bg-gray-100 text-gray-800",
    };

    return (
      <span
        className={`px-2 py-1 rounded-full text-xs font-medium ${
          styles[priority] || "bg-gray-100 text-gray-800"
        }`}
      >
        {priority}
      </span>
    );
  };

  if (loading)
    return (
      <div className="min-h-screen bg-slate-100 flex items-center justify-center">
        <p className="text-lg text-gray-600">Cargando tareas...</p>
      </div>
    );

  if (error)
    return (
      <div className="min-h-screen bg-slate-100 flex items-center justify-center">
        <p className="text-lg text-red-500">{error}</p>
      </div>
    );

  <div className="min-h-screen bg-slate-100 py-8 px-4">
    <div className="max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
        <h1 className="text-3xl font-bold text-gray-800">Panel de tareas</h1>
        <div className="flex gap-3">
          <Link
            to="tasks/new"
            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700 transition shadow-md font-medium"
          >
            Nueva tarea
          </Link>

          <button
            onClick={handLogout}
            className="bg-gray-600 text-white px-5 py-2 rounded-lg hover:bg-gray-700 transition shadow-md font-medium"
          >
            Cerrar sesión
          </button>
        </div>
      </div>

      {/* Table Container*/}
      {tasks.length === 0 ? (
        <div className="bg-white rounded-lg shadow-md p-12 text-center">
          <p className="text-gray-500 text-lg">
            No hay tareas registradas.{" "}
            <Link
              to="/tasks/new"
              className="text-green-600 hover:underline font-medium"
            >
              Crear una nueva tarea
            </Link>
          </p>
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-50 border-b">
                <tr>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Título
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Estado
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Prioridad
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Responsable
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Vence
                  </th>
                  <th className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">
                    Acciones
                  </th>
                </tr>
              </thead>

              <tbody className="bg-white divide-y divide-gray-200">
                {tasks.map((t) => (
                  <tr key={t.id} className="hover:bg-gray-50 transition-colors">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm font-medium text-gray-900">
                        {t.title}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      {getStatusBadge(t.status)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      {getPrioriryBadge(t.priority)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                      {t.assignedTo}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                      {t.dueDate}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm">
                      <div className="flex gap-2">
                        <button
                          className="bg-blue-600 text-white px-3 py-1.5 rounded hover:bg-blue-700 transition text-xs font-medium"
                          onClick={() => navigate(`/tasks/${t.id}`)}
                        >
                          Editar
                        </button>
                        <button
                          className="bg-red-600 text-white px-3 py-1.5 rounded hover:bg-red-700 transition text-xs font-medium"
                          onClick={() => handDelete(t.id)}
                        >
                          Eliminar
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  </div>;
}

export default TasksList;
