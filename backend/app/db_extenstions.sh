#!/bin/bash
set -e

echo "Initialising DB Extensions."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname="$POSTGRES_DB"<<-EOSQL
   CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOSQL

echo "DB Extensions Successfully Initialised."
