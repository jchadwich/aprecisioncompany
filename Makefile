APP := app

image:
	@docker compose build ${APP}

shell:
	@docker compose exec ${APP} /bin/bash

dbshell:
	@docker compose exec ${APP} bash -c "python3 manage.py dbshell"

repl:
	@docker compose exec ${APP} bash -c "python3 manage.py shell_plus"

migrate_db:
	@docker compose exec ${APP} bash -c "python3 manage.py migrate"

check_migrations:
	@docker compose exec ${APP} bash -c "python3 manage.py makemigrations --check"

test:
	@docker compose run --rm ${APP} bash -c "python3 manage.py test --parallel"

fmt:
	@docker compose run --rm ${APP} bash -c "black ."

check_fmt:
	@docker compose run --rm ${APP} bash -c "black --check ."

lint:
	@docker compose run --rm ${APP} bash -c "ruff ."

isort:
	@docker compose run --rm ${APP} bash -c "isort ."
