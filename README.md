# base-service

### Creating database
1. cd into db
2. export in .bash_profile the following and reload source .bash_profile
   1. export SQL_ALCHEMY_URL=postgresql://<username>:<password>@<host>:5432/<dbname>
3. pipenv install
4. pipenv run create-db
5. pipenv run alembic upgrade head - will create tables and upgrade to latest migration
6. pipenv run alembic revision --autogenerate -m <message> to create a migration