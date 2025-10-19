import json
from kafka import KafkaConsumer

consumer_conf = {
    'bootstrap_servers': ['kafka1:9092','kafka2:9092','kafka3:9092'],
    'group_id': 'aws_python_group_id',
    'auto_offset_reset': 'latest',
    'value_deserializer': lambda v: json.loads(v.decode('utf-8'))
}

consumer = KafkaConsumer('python_producer_test_topic', **consumer_conf)

for message in consumer:
    print(f"Received message: {message.value}")
consumer.closed()
