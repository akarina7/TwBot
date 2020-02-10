import tweepy

from secrets import *

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

search_text = "Python -RT"


for tweet in tweepy.Cursor(api.search,q=search_text, truncated="false").items(10) :
    try :
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            print("RT @" + tweet.user.screen_name + ":")
     #       tweet.text.encode('utf-8')
     #      print(tweet.text)
     #       status_tweet = str(unicode(tweet.text).encode("utf-8"))
            print(tweet.text)
            tweet.retweet()
    except tweepy.TweepError as er:
        print(er.reason)
        
