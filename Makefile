.PHONY: test

run:
	. venv/Scripts/activate; python manage.py runserver

test:
	pytest -v tests/

init:
	python -m venv venv;source venv/bin/activate;pip install --upgrade pip;pip install -r requirements.txt --upgrade

venv:
	. venv/Scripts/activate;
