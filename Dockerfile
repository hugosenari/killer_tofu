FROM alpine
RUN apk add --no-cache python3
RUN apk add --no-cache python3-dev
RUN apk add --no-cache g++
RUN pip3 install --upgrade pip
COPY . /src
RUN pip3 install -r /src/requirements.txt
ENV MUFFIN_CONFIG=killer_tofu.settings.production
WORKDIR /src/
ENTRYPOINT muffin killer_tofu run
EXPOSE 5000