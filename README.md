# TODO API
Simple REST API based on python3, FastAPI and PostgreSQL.

## Environment
Application requires _python 3.7_, _docker_ and _make_ to be installed.

## How to run server
```bash
$ git clone https://github.com/ivanpobeguts/todo_api.git
$ make run-db
$ make run
```
This command will start server on 127.0.0.1:8000

## API
API documentation should be available on http://0.0.0.0:8000/docs .

## Tests
Then you can run all the tests using command:
```bash
$ make test
```