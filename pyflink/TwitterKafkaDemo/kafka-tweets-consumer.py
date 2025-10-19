from kafka import KafkaConsumer
from json import loads
from rich import print

# Create a Kafka consumer
consumer = KafkaConsumer(
    'stream-twitter-events',
    bootstrap_servers = ['kafka1:9092','kafka2:9092','kafka3:9092'],
    auto_offset_reset = 'latest',
    enable_auto_commit = True,
    group_id = None,
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)

# Process incoming messages
for message in consumer:
    tweet = message.value
    print(tweet)
