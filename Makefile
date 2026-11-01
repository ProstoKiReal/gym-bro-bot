up:
	docker compose up --build -d

ruff-lint:
	uv run ruff check --fix src

ruff-format:
	uv run ruff format src

ruff: ruff-format ruff-lint