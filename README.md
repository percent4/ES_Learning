### Author

- Jclian91

### 介绍

`Elasticsearch`和`Kibana`, `ELK`, `Kafka`学习笔记，编程语言为Python.

### 环境搭建

ElasticSearch以及Kibana的版本为8.13.0, 配置参考`docker-compose.yml`文件，启动命令：`docker-compose up -d`.

ik分词器的配置参考es/ik/config/IKAnalyzer.cfg.xml.

可视化工具：Kibana, elasticsearch-head(有对应的Chrome插件)

### ES文件说明

- 基础操作: `basic_operation.py`
- 数据批量插入: `batch_data_insert.py`
- 部分有用的命令: `useful_command.md`

### ELK相关

Beats -> Logstash -> ElasticSearch -> Kibana

启动命令: `docker-compose -f elk-docker-compose.yml`.

![elk](https://s2.loli.net/2025/04/24/2ZQIfYusF6zSMBb.png)

### Eland 相关

Eland for Machine Learning. Use `eland-docker-compose.yml` for environment preparation.

command:

```bash
docker run -itd --rm docker.elastic.co/eland/eland \
	eland_import_hub_model --url http://localhost:9200 \ 
	--hub-model-id shibing624/bert4ner-base-chinese \
	--task-type ner \
	--start \
	--clear-previous
```

### Kafka相关

3.9.0 版本: 需要Zookeeper, 参考文章[Kafka入门（一）Kafak介绍、安装与简单使用](https://zhuanlan.zhihu.com/p/19882905684)

4.0.0 版本: 不带Zookeeper, 配置文件参考`kafka/kafka-docker-compose.yml`，启动命令为`docker-compose -f kafka-docker-compose.yml up -d`.

3.9.0版本的可视化工具为Offset Explorer，4.0.0版本的可视化工具为kafka-ui，已配置在`kafka/kafka-docker-compose.yml`中。

基本操作文件:

- producer.py: 生产者
- consumer.py: 消费者

kafka-ui可视化截图：

![](https://s2.loli.net/2025/04/24/RiY93EAmILj8BXO.png)


### 文档

#### 参考docs目录:

1. elk入门笔记1.md
2. Kibana中的可视化数据分析功能.md
3. 使用ElasticSearch进行自然语言处理：以命名实体识别为例.md

#### ELK相关文章

1. [ELK入门教程（一）](https://zhuanlan.zhihu.com/p/673877455)
2. [ELK学习笔记（二）数据同步](https://zhuanlan.zhihu.com/p/673883520)
3. [ELK学习笔记（三）Beats家族](https://zhuanlan.zhihu.com/p/19888133302)

#### Kafka相关文章

1. [Kafka入门（一）Kafak介绍、安装与简单使用](https://zhuanlan.zhihu.com/p/19882905684)
2. [Kafka入门（二）ELK遇上Kafka：日志分析最佳实践](https://zhuanlan.zhihu.com/p/21595183967)
3. [Kafka入门（三）Kafka 在 Web 应用中的实践：基于 FastAPI 实现图片 OCR](https://zhuanlan.zhihu.com/p/22684936110)
4. [Kafka入门（四）Kafka消息消费状态全解析：如何精准追踪你的数据流向？](https://zhuanlan.zhihu.com/p/22686795434)
