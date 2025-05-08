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
            "is_complete": bool(self.completed_at)
        } 

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

    
