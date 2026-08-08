from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from task_manager_cli.database import Base
from task_manager_cli.models import TaskPriority, TaskStatus
from sqlalchemy import func

class TaskDB(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(default=TaskStatus.PENDING)
    priority: Mapped[str] = mapped_column(default=TaskPriority.MEDIUM)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())