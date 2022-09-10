#################################################################################
# GLOBALS                                                                       #
#################################################################################
ENVNAME := .venv
VENV := $(ENVNAME)/bin

PROJECT_NAME = abhakliste
PYTHON_INTERPRETER = $(VENV)/python

#################################################################################
# COMMANDS                                                                      #
#################################################################################
.PHONY: run
run:
	$(PYTHON_INTERPRETER) src/abhakliste/main.py

.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

	rm -rf .*_cache
	rm -rf logs
	rm -rf site

.PHONY: test
test:
	$(PYTHON_INTERPRETER) -m pytest src/tests

.PHONY: lint
lint:
	git add --intent-to-add .
	$(VENV)/pre-commit run --all-files
