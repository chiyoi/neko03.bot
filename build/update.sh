#!/bin/zsh
git pull
docker pull chiyoi/atri_bot-gocq
./build-image.sh
./docker-entry.sh
