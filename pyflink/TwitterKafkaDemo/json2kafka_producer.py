import json
from time import sleep
from rich import print
from kafka import KafkaProducer

# Define the path to the json file
json_file_path = 'twitter_data.json'

producer_conf = {
    'bootstrap_servers': ['kafka1:9092','kafka2:9092','kafka3:9092'],
    'value_serializer': lambda v: json.dumps(v).encode('utf-8')
}

producer = KafkaProducer(**producer_conf)

# Read the JSON file
with open(json_file_path, 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        tweet_data = json.loads(line)
        producer.send('stream-twitter-events', value=tweet_data)  # Send data to Kafka topic
        print(tweet_data)  # Print the tweet data
        sleep(0.5)  # Pause for 0.5 seconds before processing the next tweet

# Close the producer
producer.flush()
producer.close()
