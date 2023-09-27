#!/bin/sh


# echo "Flush the manage.py command it any"

# while ! python manage.py flush --no-input 2>&1; do
#   echo "Flusing django manage command"
#   sleep 3
# done

#echo "Make Migrations Database at startup of project"
#
#while ! python manage.py makemigrations 2>&1; do
#  echo "Make Migrations Database"
#  sleep 3
#done
#
#echo "Migrate the Database at startup of project"
# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"

#uwsgi --socket :8000 --master --enable-threads --module mysite.wsgi