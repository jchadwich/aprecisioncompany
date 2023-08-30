APP := app

network:
	@docker network create aprecisioncompany-dev || true

image:
	@docker compose build ${APP}

shell:
	@docker compose exec ${APP} /bin/bash

dbshell:
	@docker compose exec ${APP} bash -c "dj dbshell"

repl:
	@docker compose exec ${APP} bash -c "dj shell_plus --ipython"

migrate_db:
	@docker compose exec ${APP} bash -c "dj migrate"

check_migrations:
	@docker compose exec ${APP} bash -c "dj makemigrations --check"

test:
	@docker compose run --rm ${APP} bash -c "dj test --parallel"

fmt:
	@docker compose run --rm ${APP} bash -c "black ."

check_fmt:
	@docker compose run --rm ${APP} bash -c "black --check ."

lint:
	@docker compose run --rm ${APP} bash -c "ruff ."

isort:
	@docker compose run --rm ${APP} bash -c "isort ."
