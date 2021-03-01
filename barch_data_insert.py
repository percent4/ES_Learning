# -*- coding: utf-8 -*-
# @Time : 2021/3/1 21:37
# @Author : Jclian91
# @File : barch_data_insert.py
# @Place : Yangpu, Shanghai
import time
import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

total_context = ["美国留给伊拉克的是个烂摊子吗"] * 10000

es = Elasticsearch(hosts="192.168.4.193:9200")
mapping = {
    "mappings": {
        "properties": {
            "context": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_smart"
                }
        }
    }
}
es.indices.delete(index='test', ignore=[400, 404])
resp = es.indices.create(index='test', body=mapping, ignore=400)
print(resp)

# batch record insert
s_time = time.time()
action = ({
            "_index": "test",
            "_type": "_doc",
            "_source": {
                "context": _,
                "insert_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
         } for _ in total_context)
helpers.bulk(es, action)
e_time = time.time()
print(f"cost time: {e_time-s_time}")
# 批量插入10000条数据耗时: 17.75s

# single record insert
# s_time = time.time()
# data_list = [{"context": _, "insert_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} for _ in total_context]
# for i, data in enumerate(data_list):
#     print(f"insert {i} record of data")
#     es.index(index='test', body=data)
# e_time = time.time()
# print(f"cost time: {e_time-s_time}")
# 单次插入10000条数据耗时: 2345.98s
