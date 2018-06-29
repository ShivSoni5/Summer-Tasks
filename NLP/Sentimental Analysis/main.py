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

tweets = extractor.user_timeline(screen_name = "maddhruv", count = 20)
print(f"Number of tweets extracted: {len(tweets)}.\n")
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()
