#!/usr/bin/python3

import tweepy
import pandas as pd
import numpy as np
from textblob import TextBlob
import re
from IPython.display import display
import matplotlib.pyplot as plt
from credentials import *

def twitter_setup():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

tweets = extractor.user_timeline(screen_name = "realDonaldTrump", count = 20)
'''
print(f"Number of tweets extracted: {len(tweets)}.\n")
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()
'''
# we create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# we add relevent data:
data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])

# we display the first 10 elements of the dataframe:
#display(data.head(10))

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

data['SA'] = np.array([analize_sentiment(tweet) for tweet in data['Tweets']])

display(data.head(10))

# we construct lists with classified tweets:

pos_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0 ]
neu_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0 ]
neg_tweets = [tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0 ]

# we print percentages:

print (f"Percentage of positive tweets: {len(pos_tweets)*100/len(data['Tweets'])}%")
print (f"Percentage of neutral tweets: {len(neu_tweets)*100/len(data['Tweets'])}%")
print (f"Percentage of negative tweets: {len(neg_tweets)*100/len(data['Tweets'])}%")

