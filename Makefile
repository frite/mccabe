checkfiles = mcc/ tests/ conftest.py build.py
py_warn = PYTHONDEVMODE=1

up:
	poetry update

deps: clean
	git submodule init
	git submodule update
	poetry install

style: deps
	isort -src $(checkfiles)
	black $(checkfiles)

check: deps
	black --check $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
	pflake8 $(checkfiles)
	bandit -x tests -r $(checkfiles)
	mypy $(checkfiles)

test: deps
	$(py_warn) pytest --cov

build: clean
	poetry build

clean:
	rm -rf ./dist ./build

benchmark: deps
	python benchmark/main.py

ci: check test
