import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

import TaskList from "../../components/TaskList";
import { sampleTasks } from "../fixtures/tasks";

describe("TaskList - interacciones del usuario", () => {
  it("dispara onToggle al marcar completado", async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    render(<TaskList tasks={sampleTasks} onToggle={onToggle} onDelete={() => {}} />);

    await user.click(screen.getByLabelText(/preparar clase/i));

    expect(onToggle).toHaveBeenCalledWith("t1");
  });

  it("dispara onDelete al eliminar", async () => {
    const user = userEvent.setup();
    const onDelete = vi.fn();
    render(<TaskList tasks={sampleTasks} onToggle={() => {}} onDelete={onDelete} />);

    await user.click(screen.getAllByRole("button", { name: /eliminar/i })[0]);

    expect(onDelete).toHaveBeenCalledWith("t1");
  });

  it("permite navegar con teclado y activar checkbox", async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    render(<TaskList tasks={sampleTasks} onToggle={onToggle} onDelete={() => {}} />);

    await user.tab();
    await user.keyboard("[Space]");

    expect(onToggle).toHaveBeenCalledWith("t1");
  });
});
