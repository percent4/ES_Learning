# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: topic_cmd.py
# @time: 2025/1/22 16:22
from kafka.admin import KafkaAdminClient

# 创建 KafkaAdminClient 实例
admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092', client_id='admin-client')

# 获取所有 topic 列表
topics = admin_client.list_topics()
print("所有 Topic:", topics)
results = admin_client.describe_topics(topics)
for detail in results:
    if detail['topic'] == "__consumer_offsets":
        continue
    print("Topic 详情:", detail)

admin_client.close()
