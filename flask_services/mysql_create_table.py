# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: mysql_create_table.py
# @time: 2023/12/23 23:29
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(INTEGER)
    place = Column(VARCHAR(256), nullable=False)
    insert_time = Column(DATETIME)

    def __init__(self, id, name, age, place, insert_time):
        self.id = id
        self.name = name
        self.age = age
        self.place = place
        self.insert_time = insert_time


def init_db():
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/orm_test",
        echo=True
    )
    Base.metadata.create_all(engine)
    print('Create table successfully!')


if __name__ == '__main__':
    init_db()
