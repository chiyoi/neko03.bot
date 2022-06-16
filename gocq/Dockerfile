FROM golang:1.18-alpine

WORKDIR /build
COPY ./go-cqhttp/ ./
RUN GO111MODULE=auto CGO_ENABLED=0 go build -ldflags "-s -w -extldflags '-static'" -o /target/go-cqhttp

FROM alpine

WORKDIR /tmp
RUN apk add --no-cache ffmpeg

WORKDIR /gocq
COPY --from=0 /target/go-cqhttp ./

WORKDIR /gocq/neko0001
CMD ["../go-cqhttp", "--faststart"]
