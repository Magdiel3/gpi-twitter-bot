import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    """Authenticate Twitter API for any usage

    Returns
    -------
    Twitter API
       Authenticated Twitter API
    """
    
    # Load environment variables
    tw_api_key = os.getenv("TWITTER_API_KEY")
    tw_api_secret = os.getenv("TWITTER_API_SECRET")
    tw_access_key = os.getenv("TWITTER_ACCESS_TOKEN")
    tw_access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(tw_api_key,tw_api_secret)
    auth.set_access_token(tw_access_key,tw_access_secret)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    # Verify credentials and raise errors
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    
    logger.info("API created")

    return api