# Python SQLAlchemy, alembic & psycopg2 demo

This repo contains a demo to see the scenarios to use SQLAlchemy and psycopg2. Likewise, it show the use of alembic a tool to execute migrations. 

``docker run  -e POSTGRES_PASSWORD=password -e POSTGRES_HOST_AUTH_METHOD=trust -v $PWD/data:/var/lib/postgresql/data -v $PWD/init.sql:/docker-entrypoint-initdb.d/init.sql -p 5432:5432 --name postgres_local postgres``
