from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='jc',
                         sasl_plain_password='jckafka')
for i in range(10):
    message = f'Hello {i} from Kafka.'.encode('utf-8')
    producer.send(topic='school', value=message)
producer.close()
