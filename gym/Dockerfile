FROM python:3.6-slim-stretch

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt-get update && apt-get install -y cmake libopenmpi-dev python3-dev zlib1g-dev \
libgl1-mesa-glx libglib2.0-0

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./main.py" ]