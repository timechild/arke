#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
	CREATE DATABASE arke;
	GRANT ALL PRIVILEGES ON DATABASE arke TO postgres;
EOSQL