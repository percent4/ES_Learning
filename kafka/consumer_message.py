# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: consumer_message.py
# @time: 2025/2/8 10:52
from kafka import KafkaConsumer, KafkaAdminClient, TopicPartition

topic = "ocr-topic"
group_id = "ocr-group"
bootstrap_servers = ["localhost:9092"]

# 创建 KafkaConsumer，但不订阅 topic，而是手动指定分区
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    group_id=group_id
)

# 获取 topic 的所有分区
partitions = consumer.partitions_for_topic(topic)
if partitions is None:
    print(f"无法获取 topic {topic} 的分区信息")
    exit(1)

# 为每个分区创建一个 TopicPartition 对象
topic_partitions = [TopicPartition(topic, p) for p in partitions]

# 查询每个分区的最新 offset（Log End Offset）
end_offsets = consumer.end_offsets(topic_partitions)

# 查询消费组的 committed offset（已消费的消息偏移量）
committed_offsets = {tp: consumer.committed(tp) for tp in topic_partitions}

# 计算 LAG（未消费的消息数量）
for tp in topic_partitions:
    committed_offset = committed_offsets.get(tp, 0) or 0  # 可能返回 None，需要转换为 0
    end_offset = end_offsets[tp]
    lag = end_offset - committed_offset
    print(f"Partition {tp.partition}: Log End Offset = {end_offset}, Committed Offset = {committed_offset}, LAG = {lag}")

# 关闭消费者
consumer.close()

# 输出结果示例：
# Partition 0: Log End Offset = 23, Committed Offset = 23, LAG = 0
