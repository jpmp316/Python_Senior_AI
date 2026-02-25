import { FormEvent, useState } from "react";

export type TaskFormProps = {
  onCreateTask: (title: string) => void | Promise<void>;
};

export default function TaskForm({ onCreateTask }: TaskFormProps) {
  const [title, setTitle] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const trimmedTitle = title.trim();
  const isDisabled = isSubmitting;

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!trimmedTitle) {
      setError("La tarea es obligatoria.");
      return;
    }
    setError(null);
    setIsSubmitting(true);
    try {
      await onCreateTask(trimmedTitle);
      setTitle("");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} aria-label="Formulario de tareas">
      <label htmlFor="task-title">Nueva tarea</label>
      <input
        id="task-title"
        name="task-title"
        type="text"
        value={title}
        onChange={(event) => {
          const value = event.target.value;
          setTitle(value);
          if (error && value.trim()) {
            setError(null);
          }
        }}
        aria-invalid={error ? "true" : "false"}
        aria-describedby={error ? "task-title-error" : undefined}
        placeholder="Escribe una tarea"
      />
      {error ? (
        <p role="alert" id="task-title-error">
          {error}
        </p>
      ) : null}
      <button type="submit" disabled={isDisabled}>
        Crear tarea
      </button>
    </form>
  );
}
