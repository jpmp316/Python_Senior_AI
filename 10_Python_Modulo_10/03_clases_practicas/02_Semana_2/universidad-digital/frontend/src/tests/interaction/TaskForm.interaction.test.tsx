import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import TaskForm from "../../components/TaskForm";

describe("TaskForm - interacciones del usuario", () => {
  it("permite escribir y enviar con click", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    await user.type(screen.getByRole("textbox", { name: /nueva tarea/i }), "Estudiar React");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(onCreateTask).toHaveBeenCalledWith("Estudiar React");
  });

  it("permite enviar con Enter", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    const input = screen.getByRole("textbox", { name: /nueva tarea/i });
    await user.type(input, "Enviar con Enter{enter}");

    expect(onCreateTask).toHaveBeenCalledWith("Enviar con Enter");
  });

  it("no envía si solo hay espacios", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    await user.type(screen.getByRole("textbox", { name: /nueva tarea/i }), "   ");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(onCreateTask).not.toHaveBeenCalled();
    expect(screen.getByRole("alert")).toBeVisible();
  });

  it("permite múltiples envíos", async () => {
    const user = userEvent.setup();
    const onCreateTask = vi.fn();
    render(<TaskForm onCreateTask={onCreateTask} />);

    const input = screen.getByRole("textbox", { name: /nueva tarea/i });
    await user.type(input, "Tarea 1");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));
    await user.type(input, "Tarea 2");
    await user.click(screen.getByRole("button", { name: /crear tarea/i }));

    expect(onCreateTask).toHaveBeenCalledTimes(2);
  });
});
