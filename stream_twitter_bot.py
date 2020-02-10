#import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#from tweepy import API
#from tweepy import cursor

from secrets import *

### TWITTER CLIENT ###
class TwitterClient() :
    
    def __init__(self) :
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def org_tweets(self, fetched_tweets_file) :
        tweetDB = open(fetched_tweets_file, "r")
        for line in tweetDB :
            element = line.split(',"text":"')[1].split('","source')[0]
            print(element)
          

### TWITTER AUTHENTICATOR ###
class TwitterAuthenticator() :
    def authenticate_twitter_app(self) :
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return auth

### TWITTER STREAMER ###
class TwitterStreamer() :
    '''
    Class for streaming and processing live tweets.
    '''
    def __init__(self) :
        self.twitter_authenticator = TwitterAuthenticator()
        
    def stream_tweets(self, fetched_tweets_file, search_text) :
        #handles twitter authentication and connection to the twitter streamer API
        listen = listener(fetched_tweets_file)
        
        auth = self.twitter_authenticator.authenticate_twitter_app()
        twitterStream = Stream(auth, listen)
        twitterStream.filter(track=[search_text])

### TWITTER LISTENER ###
class listener(StreamListener) :
    '''
    prints received tweets to the listener
    '''
    def __init__(self, fetched_tweets_file) :
        self.fetched_tweets_file = fetched_tweets_file
        
    def on_data(self, data) :
        try :
            #print(data)
            if "RT @" in data :
                pass
            else :
                print(data)
                with open(self.fetched_tweets_file, "a") as tf :
                    tf.write(data)
                return True
        except BaseException as e :
            print("Error on_data %s" % str(e))
        return True
    
    def on_error(self, status) :
        if status == 420 :
            # if the data method reaches rate limit occurs
            return False
        print(status)

if __name__ == "__main__" :
    
    search_text = "Python"
    fetched_tweets_file = "tweets.txt"

    #below is old
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_file, search_text)

    #below is new
 #   twitter_client = TwitterClient()
 #   twitter_client.org_tweets(fetched_tweets_file)
