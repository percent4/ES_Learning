# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: consumer.py
# @time: 2025/1/9 14:11
from kafka import KafkaConsumer

consumer = KafkaConsumer('sdtest', bootstrap_servers='localhost:9092')
for message in consumer:
    print(message)
    # print(f'Received message: {message.value.decode("utf-8")}')
