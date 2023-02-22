#!/bin/bash

docker rm -f nlpc
docker build -t nlpd-1 .
docker run -it -p 7777:22 -p 3333:3333 -p6060:8080 --gpus all --name nlpc nlpd-1 bash
