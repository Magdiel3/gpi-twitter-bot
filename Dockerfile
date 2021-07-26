FROM python:3.6-slim

RUN apt-get update && apt-get install -y unixodbc-dev gcc g++

COPY config.py /bots/
COPY autoreply_gpi.py /bots/
COPY requirements.txt /tmp
COPY predict_sentiment.py /bots/

RUN pip install -r /tmp/requirements.txt

RUN python -c 'import flair; _ = flair.models.TextClassifier.load("en-sentiment")'

WORKDIR /bots
CMD ["python", "autoreply_gpi.py"]