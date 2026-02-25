import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import TaskForm from "../../components/TaskForm";
import { createTask } from "../../services/taskService";

vi.mock("../../services/taskService", () => ({
  createTask: vi.fn()
}));

describe("TaskForm - cambios en UI", () => {
  it("muestra error si el input está vacío", async () => {
    const user = userEvent.setup();
    render(<TaskForm onCreateTask={vi.fn()} />);

    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(screen.getByRole("alert")).toHaveTextContent(/obligatoria/i);
  });

  it("limpia el campo después del submit exitoso", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    const input = screen.getByRole("textbox", { name: /nueva tarea/i });
    await user.type(input, "Limpiar input");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(input).toHaveValue("");
  });

  it("acepta texto largo", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    const longText = "x".repeat(120);
    await user.type(screen.getByRole("textbox", { name: /nueva tarea/i }), longText);
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(onCreateTask).toHaveBeenCalledWith(longText);
  });

  it("usa función async simulada con vi.fn()", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn().mockResolvedValue(undefined);
    render(<TaskForm onCreateTask={onCreateTask} />);

    await user.type(screen.getByRole("textbox", { name: /nueva tarea/i }), "Async task");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(onCreateTask).toHaveBeenCalledWith("Async task");
  });

  it("muestra cómo usar vi.mock para una función de servicio", async () => {
    const user = userEvent.setup();
    const mockedCreateTask = vi.mocked(createTask);
    mockedCreateTask.mockResolvedValue({
      id: "srv-1",
      title: "Desde servidor",
      completed: false
    });

    const handleCreate = async (title: string) => {
      await createTask(title);
    };

    render(<TaskForm onCreateTask={handleCreate} />);
    await user.type(screen.getByRole("textbox", { name: /nueva tarea/i }), "Desde servidor");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(mockedCreateTask).toHaveBeenCalledWith("Desde servidor");
  });
});
