FROM alpine
COPY requirements.txt /src/requirements.txt
RUN apk add --no-cache python3 python3-dev g++ &&\
    pip3 install --upgrade pip &&\
    pip3 install -r /src/requirements.txt &&\
    apk del python3-dev g++
ENV MUFFIN_CONFIG=killer_tofu.settings.production
WORKDIR /src/
EXPOSE 5000