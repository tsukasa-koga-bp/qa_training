format:
	poetry run ruff check --fix .
	poetry run black .
test:
	poetry run pytest .