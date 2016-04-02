import tweepy
import tweet
import tweet_listener
from keys import keys

# Authentication details
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

if __name__ == '__main__':

    # Create authentication token using our details
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Get API handler
    api = tweepy.API(auth)
    tweet = tweet.Tweet(api)

    t_list = tweet_listener.TweetListener(tweet)

    stream = tweepy.Stream(auth, t_list)
    stream.filter(track=['@avispamiento', '#avispamiento', '#stopvespa'])