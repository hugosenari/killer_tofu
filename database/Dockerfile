FROM alpine:edge
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN mkdir -p /data/db
RUN echo "===============COFFE TIME... :(==============="&&\
    apk add --no-cache mongodb
WORKDIR /data/db
EXPOSE 27017