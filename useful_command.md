### 基础命令

- 查看ElasticSearch是否启动成功：

curl http://IP:9200

- 查看集群是否健康

curl http://IP:9200/_cat/health?v

- 查看ElasticSearch所有的index

curl http://IP:9200/_cat/indices

- 查看ElasticSearch所有indices或者某个index的文档数量

curl http://IP:9200/_cat/count?v

curl http://IP:9200/_cat/count/some_index_name?v

- 查看每个节点正在运行的插件信息

curl http://IP:9200/_cat/plugins?v&s=component&h=name,component,version,description

- 查看ik插件的分词结果

curl -H 'Content-Type: application/json'  -XGET 'http://IP:9200/_analyze?pretty' -d '{"analyzer":"ik_max_word","text":"美国留给伊拉克的是个烂摊子吗"}'

### index操作

- 查看某个index的mapping

curl http://IP:9200/some_index_name/_mapping

- 查看某个index的所有数据

curl http://IP:9200/some_index_name/_search

- 按ID进行查询

curl -X GET http://IP:9200/索引名称/文档类型/ID

- 检索某个index的全部数据

curl http://IP:9200/索引名称/_search?pretty

curl -X POST http://IP:9200/索引名称/_search?pretty -d "{\"query\": {\"match_all\": {} }}"

- 检索某个index的前几条数据(如果不指定size,则默认为10条)

curl -XPOST IP:9200/索引名称/_search?pretty -d "{\"query\": {\"match_all\": {} }, \"size\" : 2}"

- 检索某个index的中间几条数据(比如第11-20条数据)

curl -XPOST IP:9200/索引名称/_search?pretty -d "{\"query\": {\"match_all\": {} }, \"from\" : 10, \"size\" : 10}}"

- 检索某个index, 只返回context字段

curl -XPOST IP:9200/索引名称/_search?pretty -d "{\"query\": {\"match_all\": {} }, \"_source\": [\"context\"]}"

- 删除某个index

curl -XDELETE 'IP:9200/index_name'

### ES搜索

1. 如果有多个搜索关键字， Elastic 认为它们是or关系。
2. 如果要执行多个关键词的and搜索，必须使用布尔查询。

```bash
$ curl 'localhost:9200/索引名称/文档类型/_search'  -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "content": "软件" } },
        { "match": { "content": "系统" } }
      ]
    }
  }
}'
```

3. 复杂搜索：

SQL

```sql
select * from test_index where name='tom' or (hired =true and (personality ='good' and rude != true ))
```

DSL:

```sql
GET /test_index/_search
{
    "query": {
            "bool": {
                "must": { "match":{ "name": "tom" }},
                "should": [
                    { "match":{ "hired": true }},
                    { "bool": {
                        "must":{ "match": { "personality": "good" }},
                        "must_not": { "match": { "rude": true }}
                    }}
                ],
                "minimum_should_match": 1
            }
    }
}
```

4. 模糊搜索：[https://blog.csdn.net/UbuntuTouch/article/details/101287399](https://blog.csdn.net/UbuntuTouch/article/details/101287399)

