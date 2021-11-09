clean:
	find . -name '*.pyc' -delete
	docker system prune

test:
	-pytest

run-db:
	docker-compose up -d

stop-db:
	docker-compose down

check-types:
	mypy src/ tests/

check-styles:
	flake8 src/ tests/

run:
	uvicorn src.main:app