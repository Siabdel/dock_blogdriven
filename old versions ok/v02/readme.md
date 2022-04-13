sudo docker run -ti dock_testdriven_web bash
sudo docker-compose run web django-admin startproject problog
# se connecter a la console du docker 
sudo docker run -ti dock_testdriven_web bash
sudo docker run -ti -p 8000:80 dock_testdriven_web
## create superuser
$ docker-compose run --rm app python manage.py createsuperuser
# tester la base
# 1. demarrer le docker
$ sudo  docker-compose up --build -d
# 2. se connecter a pg via psql
$ su - postgres -c "psql -f /home/django/Documents/www/docker/dock_markoblog/dbcreate.sql;"
sudo docker exec -ti dock_testdriven_web_1 bash
sudo docker-compose up --build -d
sudo docker-compose down -v
