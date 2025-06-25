FROM python:3.12.3 

# working directory in container
WORKDIR /app

# copy py file to /app folder
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

# run
ENTRYPOINT ["python", "./docker_app.py"]

#check docker version in terminal - type docker --version
#to run docker build -t my-first-container . # including full stop
#docker ps # is something running?
#docker images # what's available?
#docker run my-first-container