from src.exceptions import NotFoundError


def test_get_all_todos_ok(mocker, client, get_all_query_results, all_todos):
    mocker.patch('src.routes.repo.get_todos', return_value=all_todos)
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == get_all_query_results


def test_get_incompleted_todos_ok(mocker, client, get_all_query_results, incompleted_todos):
    mocker.patch('src.routes.repo.get_todos', return_value=incompleted_todos)
    response = client.get("/todos/?completed=false")
    assert response.status_code == 200
    assert response.json() == [get_all_query_results[0], get_all_query_results[2]]


def test_get_completed_todos_ok(mocker, client, get_all_query_results, completed_todos):
    mocker.patch('src.routes.repo.get_todos', return_value=completed_todos)
    response = client.get("/todos/?completed=true")
    assert response.status_code == 200
    assert response.json() == [get_all_query_results[1]]


def test_get_todos_without_text(mocker, client, get_all_query_results, todos_without_text):
    mocker.patch('src.routes.repo.get_todos', return_value=todos_without_text)
    response = client.get("/todos/?with_text=false")
    assert response.status_code == 200
    assert response.json() == [get_all_query_results[2]]


def test_post_ok(mocker, client, all_todos):
    mocker.patch('src.routes.repo.create_todo', return_value=all_todos[0])
    body = {
        'text': 'Text'
    }
    response = client.post("/todos/", json=body)
    assert response.status_code == 200


def test_put_ok(mocker, client, all_todos):
    mocker.patch('src.routes.repo.mark_todo_completed', return_value=all_todos[0])
    body = {
        'completed': True
    }
    response = client.put("/todos/10", json=body)
    assert response.status_code == 200


def test_put_404(mocker, client):
    mocker.patch('src.routes.repo.mark_todo_completed', side_effect=NotFoundError)
    body = {
        'completed': True
    }
    response = client.put("/todos/10000", json=body)
    assert response.status_code == 404


def test_delete_ok(mocker, client):
    mocker.patch('src.routes.repo.delete_todo')
    response = client.delete("/todos/10")
    assert response.status_code == 204


def test_delete_404(mocker, client):
    mocker.patch('src.routes.repo.delete_todo', side_effect=NotFoundError)
    response = client.delete("/todos/1000")
    assert response.status_code == 404
