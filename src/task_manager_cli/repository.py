from sqlalchemy.orm import Session
from task_manager_cli.db_models import TaskDB
from task_manager_cli.models import Task
from sqlalchemy import select

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

def get_all_tasks(db: Session) -> list[TaskDB]:
    
    stmt = select(TaskDB)

    results = db.scalars(stmt).all()

    return list(results)