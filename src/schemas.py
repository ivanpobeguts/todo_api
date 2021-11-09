from typing import Optional

from pydantic import BaseModel


class ToDoResponseSchema(BaseModel):
    id: int
    text: Optional[str]
    completed: bool

    class Config:
        orm_mode = True


class ToDoRequestSchema(BaseModel):
    id: Optional[int]
    text: Optional[str]
    completed: Optional[bool]

    class Config:
        orm_mode = True
