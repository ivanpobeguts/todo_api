from typing import Dict, Optional

from sqlalchemy.orm import Session

from .exceptions import NotFoundError
from .models import ToDo


def get_todos(session: Session, completed: bool, contains_text: bool) -> ToDo:
    query = session.query(ToDo)
    if completed is not None:
        query = query.filter(ToDo.completed == completed)
    if contains_text is not None:
        if contains_text:
            query = query.filter(ToDo.text != None)  # noqa: E711
        else:
            query = query.filter(ToDo.text == None)  # noqa: E711
    return query.all()


def create_todo(session: Session, args: Dict) -> ToDo:
    new_todo = ToDo()
    for key, value in args.items():
        if value is not None:
            setattr(new_todo, key, value)
    session.add(new_todo)
    session.commit()
    return new_todo


def mark_todo_completed(session: Session, todo_id: int, completed) -> Optional[ToDo]:
    todo = session.query(ToDo).get(todo_id)
    if not todo:
        raise NotFoundError(f'Cannot find todo with id {todo_id}')
    todo.completed = completed
    session.commit()
    return todo


def delete_todo(session: Session, todo_id: int):
    todo = session.query(ToDo).get(todo_id)
    if not todo:
        raise NotFoundError(f'Cannot find todo with id {todo_id}')
    session.delete(todo)
    session.commit()
