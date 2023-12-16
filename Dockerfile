FROM python:3.10-slim-buster

RUN apt update
RUN apt install -y git curl ffmpeg

ENV NODE_VERSION=16.18.1
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"

WORKDIR /app

COPY setup-dl.sh setup-dl.sh
RUN sh setup-dl.sh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .
