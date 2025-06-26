FROM python:3.12.3 

# working directory in container
WORKDIR /app

# copy py file to /app folder
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

# run
ENTRYPOINT ["python", "./python_app.py"]