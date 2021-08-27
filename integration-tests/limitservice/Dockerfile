# Use an official Python runtime as a parent image
FROM python:3.7-alpine 

COPY requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN apk add  --no-cache make gcc g++ && pip install  --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app

COPY ./volumes /app

# Set the working directory to /app
WORKDIR /app
