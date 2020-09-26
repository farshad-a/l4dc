FROM fash94/snap7:custom

# set the working directory in the container
WORKDIR /src

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# command to run on container start
CMD [ "python3", "v_plcs.py" ]