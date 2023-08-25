### Getting started
This application is containerized using Docker and orchestrated locally using Docker Compose. This includes the web application and PostgreSQL database.
- Instructions to install [Docker Engine](https://docs.docker.com/engine/install/)
- Instructions to install [Docker Compose](https://docs.docker.com/compose/install/)

With Docker installed, use the following commands to get up and running:
- `make image` to build the Docker image
- `docker compose up` to start the development server and initialize the database if it doesn't exist
  * This may take ~10s to start the web server because it depends on the database
- The web server should be available at `http://localhost:8000`

### Development commands
To make development easier, the following `make` commands are available:
- `make image` to build the Docker image
- `make shell` to access the container (Ubuntu) shell
- `make dbshell` to access a PostgreSQL shell
- `make repl` to access a Python shell
- `make check_migrations` to check if any migrations are missing
- `make migrate_db` to run the database migrations
- `make test` to run the unit tests
- `make fmt` to automatically reformat according to the code standards
- `make check_fmt` to check the code formatting standards
- `make lint` to lint the application (check syntax and code standards)
- `make isort` to automatically sort the import statements
