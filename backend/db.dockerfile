FROM postgres:12
COPY ./app/db_extenstions.sh /docker-entrypoint-initdb.d/
