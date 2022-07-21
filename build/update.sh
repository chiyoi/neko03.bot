#!/bin/zsh
git pull
docker pull chiyoi/atri_bot-gocq
cd /home/chiyoi/Projects/neko03.com/www || return $?
./build-image.sh
./docker-entry.sh
