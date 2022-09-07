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

#################################################################################
# SETUP
#################################################################################

.PHONY: install
install: install_tools install_dependencies install_precommit
	@echo "Initilize direnv..."
	direnv allow

.PHONY: install_tools
install_tools:
	@echo "Install dev tools..."
	git init -q
	@sh ./scripts/install_tools.sh

.PHONY: install_dependencies
install_dependencies: install_tools
	@echo "Install dependencies..."
	@sh ./scripts/install_dependencies.sh

.PHONY: install_precommit
install_precommit:
	@echo "Install pre-commit hooks..."
	git init -q
	$(VENV)/pre-commit install
	$(VENV)/pre-commit install-hooks
