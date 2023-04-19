html:
	poetry run mkdocs build
ruff:
	poetry run ruff check --fix .