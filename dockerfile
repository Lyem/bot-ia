FROM python:3.8.0-slim

RUN apt update && apt install -y --no-install-recommends \
    git \
    curl \
    wget \
    gcc \
    ffmpeg \
    libmariadb-dev \
    vim \
    wkhtmltopdf \
    python3-pyaudio

RUN useradd -ms /bin/bash python

RUN pip install poetry

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD [ "tail", "-f", "/dev/null" ]
