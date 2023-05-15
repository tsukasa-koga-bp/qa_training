run:
	poetry run python src/qa_training/adapter/cui_app.py --enable_create_model --enable_judge_survival --configs configs

dash:
	poetry run python src/qa_training/dash_app/app.py

format:
	poetry run ruff check --fix .
	poetry run black .
test:
	poetry run pytest .