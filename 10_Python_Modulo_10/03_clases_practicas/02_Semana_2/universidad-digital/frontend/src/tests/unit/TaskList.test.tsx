import { render, screen } from "@testing-library/react";

import TaskList from "../../components/TaskList";
import { sampleTasks } from "../fixtures/tasks";

describe("TaskList - comportamiento inicial", () => {
  it("muestra estado vacío cuando no hay tareas", () => {
    render(<TaskList tasks={[]} onToggle={() => {}} onDelete={() => {}} />);

    expect(screen.getByRole("status")).toHaveTextContent(/no hay tareas/i);
  });

  it("renderiza múltiples tareas con estados visibles", () => {
    render(<TaskList tasks={sampleTasks} onToggle={() => {}} onDelete={() => {}} />);

    expect(screen.getByRole("list", { name: /lista de tareas/i })).toBeVisible();
    expect(screen.getByLabelText(/preparar clase/i)).not.toBeChecked();
    expect(screen.getByLabelText(/entregar proyecto/i)).toBeChecked();
    expect(screen.getByText(/completada/i)).toBeVisible();
    expect(screen.getAllByText(/pendiente/i)).toHaveLength(2);
  });
});
