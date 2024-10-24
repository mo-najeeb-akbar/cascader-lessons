#!/bin/bash

docker pull ubuntu:22.04
docker build -t cascaders ./
docker run -it --rm -e DISPLAY=host.docker.internal:0 -p 6006:6006 -v `pwd`:/code cascaders
