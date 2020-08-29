# FROM python:3.8.5-alpine3.12 # breaks mako
FROM python:3.7.9-alpine3.12

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make git \
    && pip install --no-cache-dir uvicorn gunicorn fastapi aiofiles python-multipart redis mako git+https://github.com/mikeboers/pyhaml \
    && apk del .build-deps gcc libc-dev make

ENV PYTHONPATH=/app

COPY . .

EXPOSE 3000

CMD ./run
