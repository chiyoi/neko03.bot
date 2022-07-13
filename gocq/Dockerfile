FROM alpine

WORKDIR /tmp
RUN apk add --no-cache ffmpeg

WORKDIR /gocq
COPY ./go-cqhttp_linux_amd64/go-cqhttp ./go-cqhttp

WORKDIR /gocq/neko0001
CMD ["../go-cqhttp", "--faststart"]
