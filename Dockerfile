FROM python:3.7-alpine

COPY config.py /bots/
COPY autoreply_gpi.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "autoreply_gpi.py"]