#!/usr/bin/python3

import tweepy
import pandas as pd
import numpy as np

from IPython.display import display
import matplotlib.pyplot as plt
from credentials import *

def twitter_setup():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

tweets = extractor.user_timeline(screen_name = "narendramodi", count = 20)
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
display(data.head(10))


