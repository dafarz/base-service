from setuptools import setup, find_packages

setup(
    name='db',
    version='0.0.1',
    packages=find_packages(exclude=['migration', 'migration.*']),
    install_requires=['sqlalchemy', 'alembic', 'psycopg2']
)
