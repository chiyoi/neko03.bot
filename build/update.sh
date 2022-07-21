#!/bin/zsh
git pull
docker pull chiyoi/neko03.bot-gocq
./build-image.sh
./docker-entry.sh
