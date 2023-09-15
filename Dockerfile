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

# we set some environment varialbles, only the non-sensitive ones
# the sensitive ones will be set at container run (DB_PASSWORD, DB_HOST, and SECRET_KEY)
ENV DB_TYPE=mysql+pymsql://
ENV DB_USER=admin
ENV DB_NAME=qa_cinema

# run app.py when the container launches
ENTRYPOINT python app.py
