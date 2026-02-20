from repository.repository_task import TaskRepository
from models.model_task import Task
from utils.validator import validate_title

class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository
        
    def create_task(self, title: str) -> None:
        clean_title = validate_title(title)
        task = Task(clean_title)
        self._repository.save(task)
    
    def list_tasks(self) -> list[Task]:
        return self._repository.get_all()

    