# Build docker image
docker build . -t autoreply-gpi-bot

# Start container
docker run -it -e TWITTER_API_KEY=$TWITTER_API_KEY \
 -e TWITTER_API_SECRET=$TWITTER_API_SECRET \
 -e TWITTER_ACCESS_TOKEN=$TWITTER_ACCESS_TOKEN \
 -e TWITTER_ACCESS_TOKEN_SECRET=$TWITTER_ACCESS_TOKEN_SECRET \
 autoreply-gpi-bot