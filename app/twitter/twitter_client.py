import tweepy
import re
import numpy as np

class TwitterClient:
    def __init__(self):
        consumer_key = 'jbn3jV7tCwfFVN9yBjQ6RUowG'
        consumer_secret = 'NeujbaScjg8IfZ061ZTZKSaFPF0zXcn2FrumquDtJWGi97SYuL'
        access_token = '336803482-2vEmrsL1GB0x4AAIUzK0Pv0knU2aq5SunaWPeDcP'
        access_token_secret = 'B85a5GUAnDgr2Lree4lFAaT3FGaRSPyEK9U15B6xLzBjr'
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def read_tweeets(self, query, max_results):
        filtered = query + "-filter:retweets"
        tweets = tweepy.Cursor(self.api.search_tweets,
                               q=filtered,
                               lang="en").items(max_results)
        filtered_tweets = [[tweet.text] for tweet in tweets]
        return filtered_tweets

