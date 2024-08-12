# Use the latest Python image
FROM python:latest

# Install jq
RUN apt-get update && apt-get install -y jq

# Install python-gitlab
RUN pip install python-gitlab

# Set the working directory
WORKDIR /opt/bridge

# Copy all the Python files to the working directory
COPY *.py /opt/bridge/

ENTRYPOINT [ "/bin/bash" ]
