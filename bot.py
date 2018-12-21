import tweepy
from keys import consumer_key, consumer_secret, access_token, access_secret
from parse import tweet
import datetime

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret
ACCESS_TOKEN = access_token
ACCESS_SECRET = access_secret

date = datetime.datetime.now()
today = date.weekday()
hour = date.hour
day = date.day
month = date.month

holidays = [[24, 12], [25, 12], [26, 12],
	  [31, 12], [1, 1], [2, 1]]

active = False

# normal behaviour
if [day, month] not in holidays:
    active = True

# library's festive hours, only tweet once daily
elif [day, month] in holidays and hour is 12:

    d = date.strftime("%B %d")
    tweet = "The library is closed today on %s. Happy holidays!🎁" % d
    active = True

if active:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(tweet)
