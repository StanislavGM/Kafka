import tweepy
from json import dumps
from kafka import KafkaProducer
from rich import print
from time import sleep

producer_conf = {
    'bootstrap_servers': ['kafka1:9092','kafka2:9092','kafka3:9092'],
    'value_serializer': lambda v: dumps(v).encode('utf-8')
}

producer = KafkaProducer(**producer_conf)

# Config to read keys from the secret.txt file

with open('secrets.txt') as file:
    for line in file:
        if '=' in line:
            key, value = line.strip().split(' = ')
            if key == 'CONSUMER_KEY':
                CONSUMER_KEY = value.strip("'")
            elif key == 'CONSUMER_SECRET':
                CONSUMER_SECRET = value.strip("'")
            elif key == 'ACCESS_TOKEN':
                ACCESS_TOKEN = value.strip("'")
            elif key == 'ACCESS_TOKEN_SECRET':
                ACCESS_TOKEN_SECRET = value.strip("'")

# Set up OAuth authentication with Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Perform a Twitter search and iterate over the tweets
cursor = tweepy.Cursor(api.search_tweets, q='music', lang="en", tweet_mode='extended').items(100)
for tweet in cursor:
    hashtags = tweet.entities['hashtags']
    hashtext = []
    for j in range(0, len(hashtags)):
        hashtext.append(hashtags[j]['text'])

    # Prepare data to be sent to Kafka topic
    cur_data = {
        "id_str": tweet.id_str,
        "username": tweet.user.name,
        "tweet": tweet.full_text,
        "location": tweet.user.location,
        "retweet_count": tweet.retweet_count,
        "favorite_count": tweet.favorite_count,
        "followers_count": tweet.user.followers_count,
        "lang": tweet.lang
    }

    producer.send('stream-twitter-events', value=cur_data)  # Send data to Kafka topic
    print(cur_data)  # Print the tweet data
    sleep(0.5)  # Pause for 0.5 seconds before processing the next tweet
