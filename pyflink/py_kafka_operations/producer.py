import json
from kafka import KafkaProducer
import time

# Config for Kafka producer
producer_conf = {
    'bootstrap_servers': ['kafka1:9092','kafka2:9092','kafka3:9092'],
    'value_serializer': lambda v: json.dumps(v).encode('utf-8')
}

# Create a producer example
producer = KafkaProducer(**producer_conf)

# Define a topic name
topic_name = 'python_producer_test_topic'

# Send Kafka message to the topic
for i in range(3):
    message = { 'this is message #:' :i } 
    producer.send(topic_name,value=message)
    print(f'Message sent:{message}')
    time.sleep(1)

# Cleanup and close the producer

producer.flush()
producer.close()
