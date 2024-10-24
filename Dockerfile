# Use an official Ubuntu base image
FROM ubuntu:22.04

# Set the environment to non-interactive mode to avoid prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

RUN set -x \
    && apt-get -y update \
    && apt-get -y install software-properties-common vim git openssh-client ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3.11
RUN set -x \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get -y update \
    && apt-get install -y python3.11-dev python3-pip python3.11-tk \
    && apt-get -y clean \
    && ln -sf /usr/bin/python3.11 /usr/bin/python \
    && ln -sf /usr/bin/python3.11 /usr/bin/python3


RUN pip install opencv-python numpy matplotlib

# Set the working directory
WORKDIR /code

ENV DISPLAY=host.docker.internal:0

# Set the entry point to bash so it opens the terminal when the container starts
ENTRYPOINT ["/bin/bash"]
