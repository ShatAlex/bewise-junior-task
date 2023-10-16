.SILENT:

build:
	docker-compose up --build
run:
	docker-compose up
db_connect:
	docker-compose exec db bash
