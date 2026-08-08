from sqlalchemy.orm import Session
from task_manager_cli.db_models import TaskDB
from task_manager_cli.models import Task

def create_task(db: Session, task: Task) -> TaskDB:

    db_task = TaskDB(
        title=task.title,
        description=task.description,
        status=task.status.value,
        priority=task.priority.value,
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task