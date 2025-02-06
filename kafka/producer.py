# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: producer.py
# @time: 2025/1/9 14:12
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(10):
    message = f'Hello {i} from Kafka.'.encode('utf-8')
    producer.send(topic='school', value=message)
producer.close()
