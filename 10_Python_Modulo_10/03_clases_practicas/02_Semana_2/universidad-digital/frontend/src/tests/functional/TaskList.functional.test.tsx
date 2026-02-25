import { render, screen } from "@testing-library/react";

import TaskList from "../../components/TaskList";
import { sampleTasks } from "../fixtures/tasks";

describe("TaskList - cambios en UI", () => {
  it("muestra lista vacía cuando no hay tareas", () => {
    render(<TaskList tasks={[]} onToggle={() => {}} onDelete={() => {}} />);

    expect(screen.getByRole("status")).toHaveTextContent(/no hay tareas/i);
  });

  it("refleja cambios cuando se re-renderiza", () => {
    const { rerender } = render(
      <TaskList tasks={sampleTasks} onToggle={() => {}} onDelete={() => {}} />
    );

    expect(screen.getByLabelText(/preparar clase/i)).toBeInTheDocument();

    rerender(<TaskList tasks={sampleTasks.slice(0, 1)} onToggle={() => {}} onDelete={() => {}} />);

    expect(screen.queryByLabelText(/entregar proyecto/i)).not.toBeInTheDocument();
  });
});
