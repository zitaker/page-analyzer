PORT ?= 8000

install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app run

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

loading:
	poetry run flask --app page_analyzer/app --debug run --port 8000