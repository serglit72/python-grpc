# Use an official Python runtime as a parent image
FROM alpine:3.7
COPY requirements.txt /tmp/
RUN apk add --no-cache g++ python && pip install --trusted-host pypi.python.org -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
