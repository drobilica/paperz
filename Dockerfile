# Start by pulling the Python image
FROM python:3.8-alpine

# Upgrade pip as root
RUN pip install --upgrade pip

# Switch working directory
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

# Configure the container to run in an executed manner
ENTRYPOINT [ "flask", "run" ]
