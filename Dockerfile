FROM python:3.9-alpine3.13
LABEL maintainer="amosokpe.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \


ENV PATH="/py/bin:$PATH"
