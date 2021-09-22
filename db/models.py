import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'

    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    text = sa.Column('text', sa.String(255))
