VENV		= .venv
# path to the Python executable inside the venv
PYTHON		= $(VENV)/bin/python
MAP			= maps/easy/01_linear_path.txt

# these names are commands, not files
.PHONY: install run debug clean lint lint-strict test

# set up the environment and install dependencies
install:
	uv venv $(VENV)
	uv pip install --python $(PYTHON) flake8 mypy pytest

# use: make run MAP=maps/easy/01_linear_path.txt
run:
	$(PYTHON) main.py $(MAP)

debug:
	$(PYTHON) -m pdb main.py $(MAP)

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache
	find . -name "*.pyc" -delete

lint:
	$(VENV)/bin/flake8 .
	$(VENV)/bin/mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(VENV)/bin/flake8 .
	$(VENV)/bin/mypy . --strict

test:
	$(PYTHON) -m pytest