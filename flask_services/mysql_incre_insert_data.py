# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai 
# @contact: lianmingjie@shanda.com
# @file: mysql_incre_insert_data.py
# @time: 2023/12/24 00:39
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql_create_table import Users
from datetime import datetime as dt


def get_time():
    time.sleep(5)
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")


def insert_data():
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/orm_test")
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()
    # 插入单条数据
    # 创建新User对象
    new_user = Users(id=8, name='Logstash', age=36, place='USA', insert_time=get_time())
    # 添加到session
    session.add(new_user)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()
    print('insert into db successfully!')


if __name__ == '__main__':
    insert_data()
