#!/usr/bin/env bash
Postgres -d http://127.0.0.1:5050/
make install && psql -a -d $DATABASE_URL -f database.sql
