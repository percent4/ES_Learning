# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: mysql_create_table.py
# @time: 2023/12/23 23:29
from datetime import datetime as dt
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(INTEGER, nullable=True)
    place = Column(VARCHAR(256), nullable=True)
    gender = Column(VARCHAR(10), nullable=True)
    insert_time = Column(DATETIME, default=dt.now())

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, place={self.place}), gender={self.gender})"


def init_db():
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/orm_test",
        echo=True
    )
    Base.metadata.create_all(engine)
    print('Create table successfully!')


if __name__ == '__main__':
    init_db()
