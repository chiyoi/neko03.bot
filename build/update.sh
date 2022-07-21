#!/bin/zsh
git pull
docker pull chiyoi/atri_bot-gocq
cd /home/chiyoi/Projects/neko03.com/bot || return $?
./build/build-image.sh
./build/docker-entry.sh
