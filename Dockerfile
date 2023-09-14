# Python image
FROM python:3.11-alpine

# set working dir
WORKDIR /app

# copy current dir content into the container at /app
COPY . /app

# install required dependencies
RUN pip install -r requirements.txt

# make port 80 available to the world outside this container
EXPOSE 5000

# run app.py when the container launches
ENTRYPOINT python app.py
