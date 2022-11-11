# justfile
#
# https://github.com/casey/just

project := "gcode_info"


# Show available commands.
help:
  @just -l


# Run the app.
run:
  poetry run {{project}}

# Run linters and formatters.
fmt:
  poetry run isort src/
  poetry run autoflake --in-place --remove-unused-variables --remove-all-unused-imports --expand-star-imports -r src/
  poetry run black src/
  poetry run flake8 src/

# Run tests.
test:
  poetry run mypy src
  poetry run pytest -v
  poetry run gcode_info tests/fixtures/files/*

# Run security scanners.
scan:
  poetry run bandit -r . -c pyproject.toml
  poetry run safety check


# First time project setup.
init:
  poetry check
  poetry install
  pre-commit install
  pre-commit install-hooks
  pre-commit autoupdate
  pre-commit run -av


# # Package using shiv.
# shiv:
#   poetry run shiv . -p '/usr/bin/env python3' -o dist/.pyz -c
#
#
# # Package using pex.
# pex:
#   pex . -o dist/.pex -c


# Remove temporary files.
clean:
  -rm dist/-*.tar.gz
  -rm dist/.pex
  -rm dist/.pyz
  -rm dist/.whl
  -rm requirements.txt
