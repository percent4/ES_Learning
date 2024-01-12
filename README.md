### Author

- Jclian91

### 介绍

`Elasticsearch`和`Kibana`, `ELK`学习笔记，编程语言为Python.

### 环境搭建

ElasticSearch以及Kibana的版本为7.x, 配置参考`docker-compose.yml`文件，启动命令：`docker-compose up -d`.

ik分词器的配置参考es/ik/config/IKAnalyzer.cfg.xml.

可视化工具：Kibana, elasticsearch-head(有对应的Chrome插件)

### 文件说明

- 基础操作: `basic_operation.py`
- 数据批量插入: `batch_data_insert.py`
- 部分有用的命令: `useful_command.md`

### ELK相关

Beats -> Logstash -> ElasticSearch -> Kibana

### 文档

参考docs目录:

1. elk入门笔记1.md
2. Kibana中的可视化数据分析功能.md
