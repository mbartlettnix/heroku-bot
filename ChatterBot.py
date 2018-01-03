# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "LqZehyBrSOwzkGx7Cpwx4mhsK"
consumer_secret = "k5taBhrfGgYNQ8ecW3JTbXibCb32f5kC375C8NF3CqAr7javKB"
access_token = "133594066-M9KUh9H6JoDyva5bkTTRt8ojaZ9dCafHc9lazW1k"
access_token_secret = "PMtstoGy0SR0yw4YqlQrge8ZRkpfy3aBeznE6WVsN8FC5"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def TweetOut(tweet_number):
	api.update_status("Happy New Year. This is a blessing to all of my friends. %s" %blessing)

blessings=("May your hearts be kept warm.","May your hearts remain open.", "May your feet be wherever you want them to be")
counter=0

while(counter<len(blessings)):
	TweetOut(blessings[counter])

	time.sleep(60)

	counter = counter + 1