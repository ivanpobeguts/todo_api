from fastapi.testclient import TestClient
import pytest

from src.models import ToDo
from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def all_todos():
    return [
        ToDo(id=10, text='Todo1', completed=False),
        ToDo(id=11, text='Todo2', completed=True),
        ToDo(id=12, text=None, completed=False)
    ]


@pytest.fixture
def incompleted_todos():
    return [
        ToDo(id=10, text='Todo1', completed=False),
        ToDo(id=12, text=None, completed=False)
    ]


@pytest.fixture
def completed_todos():
    return [
        ToDo(id=11, text='Todo2', completed=True)
    ]


@pytest.fixture
def todos_without_text():
    return [
        ToDo(id=12, text=None, completed=False)
    ]


@pytest.fixture
def get_all_query_results():
    return [
        {'id': 10, 'text': 'Todo1', 'completed': False},
        {'id': 11, 'text': 'Todo2', 'completed': True},
        {'id': 12, 'text': None, 'completed': False}
    ]
