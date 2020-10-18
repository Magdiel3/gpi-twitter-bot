import tweepy
import logging
from config import create_api
import time
from datetime import datetime


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logger = logging.getLogger()

def check_mentions(api, keywords, since_id, status="Gpi"):
    """Get new mentions since last check containing certain keywords

    Parameters
    ----------
    api : twitter api
        Authenticated Twitter api
    keywords: list(str)
        List of keywords to look up in last mentions
    since_id: int
        Last retrieved tweet
    Returns
    -------
    int
       The last tweet checked in the function call
    """

    # # Log action
    # logger.info("Retrieving mentions")

    # Update last
    new_since_id = since_id

    # Inspect all tweets since last check
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():

        new_since_id = max(tweet.id, new_since_id)

        # Tweet is not a reply
        if tweet.in_reply_to_status_id is not None:
            continue

        # Tweet matches any of the keywords
        if any(keyword in tweet.text.lower() for keyword in keywords) or not keywords:
            logger.info(f"({tweet.id}) Answering Gpi to {tweet.user.name}: {tweet.text}")

            # Reply to the matching tweet
            try:
                api.update_status(
                    status=f"@{tweet.user.screen_name} {status}",
                    in_reply_to_status_id=tweet.id,
                )
            except Exception as e:
                logger.error("Error creating tweet", exc_info=True)
            
    return new_since_id


def main():

    # Start API
    api = create_api()

    # Start from the first Tweet
    since_id = 1317697433439244293

    # Counter for printing
    count = 50

    # Remain updating and replying
    while True:
        count += 1
        if count > 25:
            logger.info(f"({since_id}) Waiting...")
            count = 1
        since_id = check_mentions(api, [], since_id)
        time.sleep(12)

if __name__ == "__main__":
    main()