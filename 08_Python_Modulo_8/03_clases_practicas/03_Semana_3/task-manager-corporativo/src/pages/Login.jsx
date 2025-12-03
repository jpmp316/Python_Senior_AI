import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!email.includes("@")) {
      setError("El email no es válido");
      return;
    }

    if (password.length < 4) {
      setError("La contrasña debe ser superior a 4 caracteres");
      return;
    }

    const fakeToken = "TOKEN_JWT_FICTICIO_123";
    localStorage.setItem("token", fakeToken);

    setError("");
    navigate("/tasks");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-md rounded p-6 w-full max-w-sm"
      >
        <h1 className="text-xl font-semibold mb-4 text-center">
          Iniciar Sesión
        </h1>

        {error && <p className="text-red-500 text-sm mb-2">{error}</p>}

        <label className="block mb-2 text-sm font-medium">
          Correo electrónico
        </label>

        <input
          className={`border rounded w-full p-2 mb-3 ${
            error && !email.includes("@") ? "border-red-500" : "border-gray-300"
          }`}
          type="email"
          placeholder="usuario@dominio.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <label className="block mb-2 text-sm font-medium">Contraseña</label>

        <input
          className={`border rounded w-full p-2 mb-4 ${
            error && password.length < 4 ? "border-red-500" : "border-gray-300"
          }`}
          type="password"
          placeholder="*******"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          type="summit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
        >
          Entrar
        </button>
      </form>
    </div>
  );
}

export default Login;
