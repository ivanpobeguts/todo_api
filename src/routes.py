from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .db import SessionLocal
from .exceptions import NotFoundError
from .models import ToDo
from . import repository as repo
from .schemas import ToDoRequestSchema, ToDoResponseSchema

todo_router = APIRouter(
    prefix="/todos",
    tags=["items"]
)


def get_session():
    session = None
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()


@todo_router.get("/", response_model=List[ToDoResponseSchema])
def get_todos(session: Session = Depends(get_session), with_text: Optional[str] = None,
              completed: Optional[str] = None) -> List[ToDo]:
    def parse_param(param):
        if param:
            if param not in ('true', 'false'):
                raise HTTPException(status_code=400, detail='Search parameters must be "true" or "false"')
            return False if param == 'false' else True
        return None

    todos = repo.get_todos(session, contains_text=parse_param(with_text), completed=parse_param(completed))
    return todos


@todo_router.post("/", response_model=ToDoResponseSchema)
def create_todo(todo: ToDoRequestSchema, session: Session = Depends(get_session)) -> ToDo:
    created = repo.create_todo(session, todo.dict())
    return created


@todo_router.put("/{todo_id}", response_model=ToDoResponseSchema)
def update_todo(todo_id: int, todo: ToDoRequestSchema, session: Session = Depends(get_session)) -> Optional[ToDo]:
    try:
        updated = repo.mark_todo_completed(session, todo_id, todo.completed)
    except NotFoundError as e:
        raise HTTPException(404, str(e))
    return updated


@todo_router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    try:
        repo.delete_todo(session, todo_id)
    except NotFoundError as e:
        raise HTTPException(404, str(e))
    return Response(status_code=204)
