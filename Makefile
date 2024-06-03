run:
	python main.py --enable_create_model --enable_judge_survival --configs configs

format:
	ruff check --fix .
	black .
test:
	pytest .