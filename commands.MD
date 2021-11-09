# Part #1

    docker build --tag python-django
    docker run --publish 8000:8000 python-django

# Part #2

    docker-compose build
    docker-compose run --rm app django-admin startproject core .
    docker-compose up
    docker exec -it django_app /bin/bash

# Part #3

    docker-compose build
    docker-compose run --rm app django-admin startproject core .
    docker compose up

## My research

In order to access a certain docker container's CLI docker

    docker container exec -it <docker name> <command>
ex: 

    docker container exec -it django_container ls
    docker container exec -it django_container /bin/bash python manage.py makemigration
    docker container exec -it django_container /bin/bash python manage.py migrate
    docker container exec -it django_container /bin/bash python manage.py createsuperuser

##### Build all my containers
    docker-compose build

##### Lifts up containers 
    docker-compose up

##### Brings down containers
    docker-compose down

### About Docker:
To list my containers

    docker ps (shows all running containers)
    docker ps -a (shows all containers)

To remove a container (needs to be bring down before)
    
    docker rm <id or container_name>





