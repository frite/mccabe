checkfiles = CyclomaticComplexity/ tests/ conftest.py
py_warn = PYTHONDEVMODE=1

up:
	@poetry update

deps:
	@poetry install

style: deps
	poetry run isort -src $(checkfiles)
	poetry run black $(checkfiles)

check: deps
	poetry run black --check $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
	poetry run pflake8 $(checkfiles)
	poetry run bandit -x tests -r $(checkfiles)
	poetry run mypy $(checkfiles)

test: deps
	$(py_warn) poetry run pytest --cov

build:
	@poetry build

benchmark: deps
	@python benchmark/main.py

ci: check test
