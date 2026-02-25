export type TaskDTO = {
  id: string;
  title: string;
  completed: boolean;
};

export async function fetchTasks(): Promise<TaskDTO[]> {
  return [];
}

export async function createTask(title: string): Promise<TaskDTO> {
  return {
    id: crypto.randomUUID(),
    title,
    completed: false
  };
}
