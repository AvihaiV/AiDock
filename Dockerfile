FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt-get update -y
RUN apt-get install -y python vim zip unzip
RUN mkdir -p */tmp
WORKDIR /tmp
COPY zip_job.py ./
RUN cat /etc/lsb-release
RUN uname -m
RUN ls -l /tmp
