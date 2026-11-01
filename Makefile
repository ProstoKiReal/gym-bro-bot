up:
	docker compose up --build -d

ruff-lint:
	uv run ruff check --fix src