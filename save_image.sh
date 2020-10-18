# Build docker image
docker build . -t autoreply-gpi-bot

# Compress image
docker image save autoreply-gpi-bot:latest -o autoreply-gpi-bot.tar
gzip autoreply-gpi-bot.tar