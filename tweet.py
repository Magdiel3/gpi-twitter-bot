import tweepy
import os

# Load environment variables
tw_api_key = os.getenv("TWITTER_API_KEY")
tw_api_secret = os.getenv("TWITTER_API_SECRET")
tw_access_key = os.getenv("TWITTER_ACCESS_TOKEN")
tw_access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(tw_api_key,tw_api_secret)
auth.set_access_token(tw_access_key,tw_access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")