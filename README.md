## Recipe API

### Setup
1. Create requirements.txt with django and djangorestframework
2. Create Dockerfile and docker-compose file

### Create superuser
1. Run `docker-compose run sh -c "python manage.py createsuperuser"`

### Running migrations
1. Run `docker-compose run app sh -c "python manage.py makemigrations"` to create migrations files
2. Run `docker-compose run app sh -c "python manage.py migrate"` to run the migration

### Using Postgres instead of sqlite

#### Update requirements.txt
1. Add `psycopg2` which is the library to connect to postgres from django

#### Update Dockerfile
1. In order to install `psycopg2` we first need to install postgresql. Add it by running`RUN apk add --update --no-cache postgresql-client.
2. Also, it needs some dev dependencies (these doesn't need to be persisted). Add these by running `RUN apk add --update --no-cache --virtual .tmp-build-dependencies \
    gcc libc-dev linux-headers postgresql-dev`. Also remove those post `pip install`

#### Update settings.py
1. Update databases section and add postgres connection details using environment variables.

#### Command to wait for db
1. We need to make sure that django app makes connection to the db only after it is ready serve request hence only `depends_on` does not suffice.
2. Add custom command `wait_for_db` and check whether the connection is available or nott

#### Update docker-compose
1. Add db service with postgres image and environment details
2. Add db connection details environment variables in app service.
3. Add `depends_on`
4. Run `wait_for_db` before actually starting the django app
5. Run `migrate` before actually starting the django app which creates the tables in the postgres db
6. Read credentials from environment variable. For this run `export POSTGRES_USER=<user name>` and `export POSTGRES_PASSWORD=<password>` 