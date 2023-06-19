.SILENT:
.PHONY: help

export FLASK_DEBUG := 1
export FLASK_APP := app

docker-up: ## stand up container
	@docker-compose up

docker-down: ## tear down container
	@docker-compose down

docker-start: ## start app in container
	@docker-compose start

docker-stop: ## stop app in container
	@docker-compose stop

docker-test: ## run tests in container
	@docker-compose run api poetry run python -m pytest -vvvvv

docker-shell: ## run a shell for the flask app in container
	@docker-compose run api poetry run flask shell

run: ## start app
	@poetry run flask run

init-db: ## initialize db
	@poetry run flask db init

make-migration: ## auto-generate migrations from schema changes
	@poetry run flask db migrate

migrate: ## run current migrations
	@poetry run flask db upgrade

migrate-down: ## migrate to previous version
	@poetry run flask db downgrade

shell: ## flask shell
	@poetry run flask shell

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help