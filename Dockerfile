# # Use an official Python runtime as the base image
FROM python:3.11-slim

# Update default packages
RUN apt-get -qq update
RUN apt-get -qq install python3-opencv

# Allow statements and log messages to immediately appear in logs
ENV PYTHONUNBUFFERED True

# Set the working directory inside the container
WORKDIR /streamer_api

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv streamerVenv
# Prepend the virtual environment's Python path (/opt/venv/bin) to the system's PATH,
# so pip does not complain about installing from root.

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /streamer_api

# Expose the port your Flask app will listen on (change 5000 to your desired port if necessary)
EXPOSE 5000

# # Set the command to run your Flask app using gunicorn (or any other WSGI server)
CMD exec gunicorn --bind :5444 --workers 2 --threads 6 --timeout 0 run:app