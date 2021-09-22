from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from env_variables import SQL_ALCHEMY_URL

_db_url_without_db = '/'.join(SQL_ALCHEMY_URL.split('/')[:-1])
engine = create_engine(f'{_db_url_without_db}', isolation_level='AUTOCOMMIT', echo=True)
Session = sessionmaker(engine)


def create_database():
    db_name = SQL_ALCHEMY_URL.split('/')[-1]
    create_database_statement = f"""SELECT 'CREATE DATABASE {db_name}' 
                                    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '{db_name}')"""
    with Session() as con:
        result = con.execute(create_database_statement).fetchone()
        if result:
            con.execute(result)
        else:
            print(f'{db_name} already exists')


if __name__ == '__main__':
    create_database()
