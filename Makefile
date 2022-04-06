SHELL := /bin/bash
PYTHON := ./venv/bin/python
PIP := ./venv/bin/pip
COVERAGE := ./venv/bin/coverage

PROJECT_DEPS := requirements.txt

.PHONY: all clean install update

all: serve

install:
	$(PIP) install -r requirements.txt

upgrade:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) freeze > requirements.txt

serve: install
	$(PYTHON) manage.py runserver

test: install
	$(PYTHON) manage.py test

test-coverage: install
	$(COVERAGE) run --source='.' manage.py test