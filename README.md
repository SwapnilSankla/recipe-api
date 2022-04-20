## Recipe API

### Setup
1. Create requirements.txt with django and djangorestframework
2. Create Dockerfile and docker-compose file

### Create superuser
1. Run `docker-compose run sh -c "python manage.py createsuperuser"`

### Running migrations
1. Run `docker-compose run app sh -c "python manage.py makemigrations"` to create migrations files
2. Run `docker-compose run app sh -c "python manage.py migrate"` to run the migration