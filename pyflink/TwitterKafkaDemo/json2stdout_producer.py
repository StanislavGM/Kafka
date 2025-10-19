import json
from time import sleep
from rich import print

# Define the path to the json file
json_file_path = 'twitter_data.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    for line in file:
        # Parse each line as a JSON object
        tweet_data = json.loads(line)

        # Access the individual fields
        id_str = tweet_data['id_str']
        username = tweet_data['username']
        tweet = tweet_data['tweet']
        location = tweet_data['location']
        created_at = tweet_data['created_at']
        retweet_count = tweet_data['retweet_count']
        favorite_count = tweet_data['favorite_count']
        followers_count = tweet_data['followers_count']
        lang = tweet_data['lang']
        coordinates = tweet_data['coordinates']

        # Process the tweet data as needed
        print(f"ID: {id_str}")
        print(f"Username: {username}")
        print(f"Tweet: {tweet}")
        print(f"Location: {location}")
        print(f"Created At: {created_at}")
        print(f"Retweet Count: {retweet_count}")
        print(f"Favorite Count: {favorite_count}")
        print(f"Followers Count: {followers_count}")
        print(f"Language: {lang}")
        print(f"Coordinates: {coordinates}")
        print("--------------------")
        sleep(1)
