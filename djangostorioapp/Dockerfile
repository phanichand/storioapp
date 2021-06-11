# pull official base image
FROM python:3.7.10-alpine3.13

# set work directory
WORKDIR /usr/src/djangostorioapp


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev

# install psycopg2 dependencies
RUN apk add --no-cache \
        libressl-dev \
        libc-dev \
        musl-dev \
        openjpeg-dev jpeg-dev zlib-dev \
        libffi-dev && \
    pip install --no-cache-dir cryptography==2.1.4 && \
    apk del \
        libressl-dev \
        musl-dev \
        libffi-dev



# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

#COPY ./docker-entrypoint.sh .
#ENTRYPOINT ["/docker-entrypoint.sh"]
