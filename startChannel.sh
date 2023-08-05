#!/bin/bash
channel=$1

if [ -z "$channel" ]; then
    echo "Usage: ./startChannel.sh <channel>"
    exit 1
fi

link=$(python3 link.py $channel)
if [ -z "$link" ]; then
    echo "Invalid channel name. Available channels: CNN, FoxNews, FoxBusiness, CBCNews, AlJazeeraAmerica, CNBC"
    exit 1
fi

export DISPLAY=:0
vlc -f $link
