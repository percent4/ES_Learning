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

