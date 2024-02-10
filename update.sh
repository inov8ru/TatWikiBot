#!/bin/sh

dir="$( cd "$( dirname "$0" )" && pwd )"
filename=$dir/posted.txt
if [ ! -f $filename ]
then
    touch $filename
fi

sudo docker build -t wiki . \
&& (sudo docker stop wiki || true && sudo docker rm wiki || true) \
&& sudo docker run -d \
   -v $(pwd)/posted.txt:/app/posted.txt \
   -e PYTHONUNBUFFERED=1 \
   --name wiki --restart unless-stopped wiki \
&& sudo docker logs -f wiki
