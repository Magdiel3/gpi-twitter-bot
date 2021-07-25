# Build docker image
docker build . -t autoreply-gpi-bot

# Compress image
docker image save autoreply-gpi-bot:latest -o autoreply-gpi-bot.tar
gzip autoreply-gpi-bot.tar

# Copy image to EC2 instance
scp -i "gpi-bot-instance.pem" autoreply-gpi-bot.tar.gz ubuntu@ec2-18-224-29-202.us-east-2.compute.amazonaws.com:/tmp

# Connect to instance
ssh -i "gpi-bot-instance.pem" ubuntu@ec2-18-224-29-202.us-east-2.compute.amazonaws.com
