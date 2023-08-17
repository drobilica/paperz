#comment

.PHONY: up down clean env

env:
	pipenv shell

run: 
	rm -rf data/*.csv && pipenv run flask run

init:
	mkdir -p data/ && rm -rf data/*.csv && curl -XGET 'localhost:5000/api/generate_cache' && curl -XGET 'localhost:5000/api/get_cache_info'

install:
	pipenv update

down:
	docker-compose down

up:
	docker-compose up -d

clean: down
	docker container prune -f && docker volume prune -f && docker image rm hartija_api

build:
	docker-compose build


