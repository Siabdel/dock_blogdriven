# docker cookbook


sudo docker run -ti dock_testdriven_web bash
sudo docker-compose run web django-admin startproject problog
## se connecter a la console du docker 
sudo docker run -ti dock_testdriven_web bash
sudo docker run -ti -p 8000:80 dock_testdriven_web
## create superuser
$ docker-compose run --rm app python manage.py createsuperuser
# tester la base
*  demarrer le docker
   

$ sudo  docker-compose up --build -d

* se connecter a pg via psql


sudo docker run -it postgres  bash 
$ su - postgres -c "psql -f /home/django/Documents/www/docker/dock_markoblog/dbcreate.sql;"
sudo docker exec -ti dock_testdriven_web_1 bash
sudo docker-compose up --build -d
sudo docker-compose down -v

## $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres

 
$ sudo docker run --name mabase -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=grutil001 -e POSTGRES_DB=blogdrivendb  -p 5433:5433  -d postgres 

###
$ su postgres

 Now, launch the psql, passing as arguent the Database name ad the Username:

$ psql blogdrivendb  postgres
$ sudo docker exec -it mabase psql -Upostgres -a blogdrivendb  -c '\lAs we have named our service "postgres", we can run into the bash of the Container with just:

$ docker-compose run postgres bash
$ sudo docker  exec -ti  mabase_container bash
# contruire que le service web
$ sudo docker-compose down -v
# modifier le fichier settings
# reconstruire que l'image web
$ sudo docker-compose up --build web
# relancer le servies web et nginx
$ sudo docker-compose up  web
$ sudo docker-compose up  nginx

### demarrer tt les service sans build
$ sudo docker-compose up --no-build -d
