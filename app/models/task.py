from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] 
    description:  Mapped[str]
    completed_at: Mapped[datetime] = mapped_column(nullable=True)

    def to_dict(self):
        return {
            "id" : self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.is_complete
        } 

    @classmethod
    def from_dict(cls, dict_data_task):
        return cls(title=dict_data_task["title"], description=["description"])