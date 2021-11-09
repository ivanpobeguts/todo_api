from sqlalchemy import Column, Integer, String, Boolean

from .db import Base


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, default=None)
    completed = Column(Boolean, default=False)
