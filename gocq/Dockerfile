FROM golang:1.17

WORKDIR /build
COPY ./go-cqhttp ./
RUN CGO_ENABLED=0 go build -o ../target/go-cqhttp

FROM alpine

WORKDIR /tmp
RUN apk add ffmpeg

WORKDIR /gocq
COPY --from=0 /build/target/go-cqhttp ./

WORKDIR /gocq/neko0001
CMD ["../go-cqhttp", "--faststart"]
