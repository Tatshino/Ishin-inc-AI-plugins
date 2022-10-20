import tweepy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_handler import *

consumer_key = twitterApiKey
consumer_secret = twitterApiKeySecret
access_token = twitterAccessToken
access_token_secret = twitterAccessTokenSecret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

#api.update_status(status="This is a sample tweet using Tweepy with python")
#twitter.send_direct_message("1223467341880680449", "hello",)

def SendMsgToCreator(DMsentence):
    twitter.send_direct_message("1223467341880680449", DMsentence)

def SendTweet(sentence):
    twitter.update_status(sentence)