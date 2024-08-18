# Use the official Python base image
FROM python:3.10.4

# Set the working directory in the container
WORKDIR /container

RUN comod 755 INSTALL.sh 
RUN ./INSTALL.sh

# set locals
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LC_ALL fa_IR.UTF-8

# Copy project
COPY . .

# Run tests
Run python3 App/app.py