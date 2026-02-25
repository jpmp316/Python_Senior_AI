import { render, screen } from "@testing-library/react";

import TaskForm from "../../components/TaskForm";

describe("TaskForm - comportamiento inicial", () => {
  it("muestra el input y el botón con etiquetas accesibles", () => {
    const onCreateTask = () => {};
    render(<TaskForm onCreateTask={onCreateTask} />);

    expect(screen.getByRole("textbox", { name: /nueva tarea/i })).toBeVisible();
    expect(screen.getByRole("button", { name: /crear tarea/i })).toBeVisible();
  });

  it("inicia con el botón habilitado para validar", () => {
    const onCreateTask = () => {};
    render(<TaskForm onCreateTask={onCreateTask} />);

    expect(screen.getByRole("button", { name: /crear tarea/i })).toBeEnabled();
  });
});
