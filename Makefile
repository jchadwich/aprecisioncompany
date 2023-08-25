APP := app

image:
	@docker compose build ${APP}

shell:
	@docker compose exec ${APP} /bin/bash
