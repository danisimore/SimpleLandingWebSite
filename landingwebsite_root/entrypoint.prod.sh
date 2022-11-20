#!/bin/sh

if [ "$SQL_DATABASE" = "landing_web_site" ]
then
  echo "Watching for landing_web_site..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
    done

    echo 'PostgreSQL started'
fi

exec "$@"

