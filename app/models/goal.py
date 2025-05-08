from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]

    def to_dict(self):
        return { 
            "id" : self.id,
            "title": self.title,
        } 

    @classmethod
    def from_dict(cls, dict_data_task):
        return cls(title=dict_data_task["title"])
    
    def update_from_dict(self, dict_data_task):
        if "title" in  dict_data_task:
            self.title = dict_data_task["title"]

