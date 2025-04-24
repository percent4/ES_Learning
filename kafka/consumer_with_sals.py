from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'school',
    bootstrap_servers='localhost:9092',
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='jc',
    sasl_plain_password='jckafka'
)

for message in consumer:
    print(f'Received message: {message.value.decode("utf-8")}')
