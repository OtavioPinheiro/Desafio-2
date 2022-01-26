FROM python:3-alpine

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

# RUN apt-get update && apt-get install -y wget

# ENV DOCKERIZE_VERSION v0.6.1

# RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#     && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#     && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#     && chmod +x /usr/local/bin/dockerize

RUN apk update && apk add wget

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# RUN touch /usr/local/bin/docker-entrypoint.sh \
#     && chmod 777 /usr/local/bin/docker-entrypoint.sh \
#     && ln -s /usr/local/bin/docker-entrypoint.sh /

COPY . .
CMD [ "python", "app.py" ]