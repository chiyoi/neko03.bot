#!/bin/zsh
usage="./docker-entry.sh [\033[4m--bot-only\033[0m]"
docker stop atri
docker rm atri
docker run -d --name atri --network atrinet chiyoi/atri_bot
if test $1;then
    if test $1 = '--bot-only'; then
        return 0
    else
        echo $usage
    fi
else
    docker stop gocq
    docker rm gocq
    docker run -d --name gocq --network atrinet --volume gocq-neko0001:/gocq/neko0001 chiyoi/atri_bot-gocq
fi
