from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db
from datetime import datetime


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .goal import Goal
class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] 
    description:  Mapped[str]
    completed_at: Mapped[datetime] = mapped_column(nullable=True)
    goal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("goal.id"))
    goal: Mapped[Optional["Goal"]] = relationship(back_populates="tasks")

    def to_dict(self):
        task_dict = { 
            "id" : self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at)
        } 

        if self.goal_id:
            task_dict["goal_id"] = self.goal_id

        return task_dict

    @classmethod
    def from_dict(cls, dict_data_task):
        return cls(title=dict_data_task["title"], description=dict_data_task["description"])
    
    def update_from_dict(self, dict_data_task):
        if "title" in  dict_data_task:
            self.title = dict_data_task["title"]
        if "description" in  dict_data_task:
            self.description = dict_data_task["description"]
        if "is_complete" in  dict_data_task:
            self.completed_at = dict_data_task["is_complete"]

    def completed(self):
        self.completed_at = datetime.now()
    
    def incompleted(self):
        self.completed_at = None

    
