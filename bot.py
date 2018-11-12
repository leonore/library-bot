import tweepy
from keys import consumer_key, consumer_secret, access_token, access_secret
from parse import tweet

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret
ACCESS_TOKEN = access_token
ACCESS_SECRET = access_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(tweet)
