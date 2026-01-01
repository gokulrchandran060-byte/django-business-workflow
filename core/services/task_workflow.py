from core.models import Task


class InvalidStatusTransition(Exception):
    pass


def change_task_status(task: Task, new_status: str) -> Task:
    """
    Placeholder for workflow logic.
    Actual validation will be added in the next phase.
    """
    task.status = new_status
    task.save(update_fields=["status", "updated_at"])
    return task
