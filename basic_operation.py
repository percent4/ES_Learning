# -*- coding: utf-8 -*-

# 导入模块
import json
import time
from elasticsearch import Elasticsearch

# 连接Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 创建index
result = es.indices.create(index='news', ignore=400)
print(result)

# 删除index
# result = es.indices.delete(index='news', ignore=[400, 404])
# print(result)

# 插入数据
data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
result = es.create(index='news', doc_type='politics', id=1, body=data)
print(result)

# 更新数据, 新增date字段
data = {
    'doc': {'date': '2011-12-16'}
}
result = es.update(index='news', doc_type='politics', id=1, body=data)
print(result)

# 删除数据
result = es.delete(index='news', doc_type='politics', id=1)
print(result)

# 创建新的数据库
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)
print(result)

# 插入新的数据
datas = [
    {
        'title': '美国留给伊拉克的是个烂摊子吗',
        'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date': '2011-12-16'
    },
    {
        'title': '公安部：各地校车将享最高路权',
        'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'date': '2011-12-16'
    },
    {
        'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url': 'https://news.qq.com/a/20111216/001044.htm',
        'date': '2011-12-17'
    },
    {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date': '2011-12-18'
    }
]

for data in datas:
    es.index(index='news', doc_type='politics', body=data)

# 查询前休眠10秒，因为数据插入需要一定的时间
time.sleep(10)

# 查询数据（简单搜索）
# result = es.search(index='news', doc_type='politics')
# print(result)

# 查询数据(全文搜索)
dsl = {
    'query': {
        'match': {
            'title': '中国 领事馆'
        }
    }
}

es = Elasticsearch()
result = es.search(index='news', doc_type='politics', body=dsl)
print(json.dumps(result, indent=2, ensure_ascii=False))