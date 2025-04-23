CURRENT_TIMESTAMP:=`date +'%Y%m%d_%H:%M:%S'`

run:
	uv run uvicorn src.minimal_template.main:app --reload --host 0.0.0.0 --port 8000

dc-build:
	docker build -t timeline-api .

run-docker:
	docker run -d -p 8000:8000 timeline-api

stop-docker:
	docker stop timeline-api

dc-up:
	docker compose -f env/prod/docker-compose.yml up -d

dc-down:
	docker compose -f env/prod/docker-compose.yml down

make-migration:
	PYTHONPATH=./src uv run alembic revision --autogenerate -m "${CURRENT_TIMESTAMP} migration"

migrate:
	PYTHONPATH=./src uv run alembic upgrade head
