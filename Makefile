run:
	poetry run python cui_app.py --enable_create_model --enable_judge_survival --configs configs

format:
	poetry run ruff check --fix .
	poetry run black .
test:
	poetry run pytest .