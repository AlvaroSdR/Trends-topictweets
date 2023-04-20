import os
import pandas as pd
from searchtweets import load_credentials, gen_rule_payload, collect_results
from openpyxl import Workbook

# Set up credentials from environment variables
premium_search_args = load_credentials("twitter_keys.yaml", yaml_key="search_tweets_v2", env_overwrite=False)

# Prompt user for topic to search
search_topic = input("Enter topic to search: ")

# Define query rule
query_rule = gen_rule_payload(search_topic, results_per_call=100, tweet_fields=["created_at"], user_fields=["public_metrics"], expansions=["author_id"], max_results=100)

# Define filter function
def filter_tweets(tweets):
    filtered_tweets = []
    for tweet in tweets:
        text = tweet.text
        if any(text.startswith(word) for word in ["Who", "Why", "What", "When", "Where", "How"]):
            filtered_tweets.append(tweet)
    return filtered_tweets

# Collect tweets using searchtweets package
tweets = collect_results(query_rule, max_results=100, result_stream_args=premium_search_args)

# Create Excel file
wb = Workbook()
ws1 = wb.active
ws1.title = "All tweets"
ws2 = wb.create_sheet(title="Filtered tweets")
ws1.append(["Username", "Tweet", "Date", "Retweets", "Likes"])
for tweet in tweets:
    username = tweet.author_id
    text = tweet.text
    date = tweet.created_at
    retweets = tweet.public_metrics['retweet_count']
    likes = tweet.public_metrics['like_count']
    ws1.append([username, text, date, retweets, likes])

# Filter tweets and save to Excel
filtered_tweets = filter_tweets(tweets)
ws2.append(["Word", "Tweet"])
for tweet in filtered_tweets:
    text = tweet.text
    for word in ["Who", "Why", "What", "When", "Where", "How"]:
        if text.startswith(word):
            ws2.append([word, text])
wb.save(f"{search_topic}_tweets.xlsx")
