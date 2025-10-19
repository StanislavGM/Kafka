from kafka import KafkaConsumer
from json import loads
from rich import print
import pydoop.hdfs as hdfs

consumer = KafkaConsumer(
    'stream-twitter-events',
    bootstrap_servers = ['kafka1:9092','kafka3:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = None,
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)

hdfs_path = 'hdfs://172.31.31.82:9000/kafka_demo/tweets_data_hdfs.json'

for message in consumer:
    tweet = message.value
    print(tweet)
    with hdfs.open(hdfs_path, 'at') as file:
        print("Storing in HDFS!")
        file.write(f"{tweet}\n")
consumer.closed()
