python = venv/bin/python
pip = venv/bin/pip
pytest = venv/bin/pytest

cli_command = $(python) run_cli.py

db-migrate:
	$(cli_command) db migrate

db-upgrade:
	$(cli_command) db upgrade

db-downgrade:
	$(cli_command) db downgrade

up:
	docker-compose up -d

pull:
	docker-compose pull

down:
	docker-compose down


install: uninstall-unrequired-libraries
	$(pip) install -r requirements.txt

install-venv:
	python -m virtualenv venv --python python3

update-requirements:
	$(pip) freeze > requirements.txt

test: clean
	mkdir -p logs
	$(pytest) -vvvv tests

clean-logs:
	rm -f logs/*.log
	rm -f logs/*.log.jsonl

clean-test-reports:
	mkdir -p test_reports
	rm -f test_reports/*.xml

clean: clean-logs clean-test-reports