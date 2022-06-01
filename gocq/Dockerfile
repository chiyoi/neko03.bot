FROM golang:1.17

WORKDIR /build
RUN wget https://github.com/Mrs4s/go-cqhttp/archive/refs/tags/v1.0.0-rc1.tar.gz
RUN gzip -d v1.0.0-rc1.tar.gz; tar xf v1.0.0-rc1.tar
RUN cd go-cqhttp-1.0.0-rc1; CGO_ENABLED=0 go build -o ../target/go-cqhttp

FROM alpine

WORKDIR /tmp
RUN apk add ffmpeg

WORKDIR /gocq
COPY --from=0 /build/target/go-cqhttp ./

WORKDIR /gocq/neko0001
CMD ["../go-cqhttp", "--faststart"]
