# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.10-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    git \
    vim

# install poetry
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV POETRY_NO_INTERACTION=1

RUN pip install pipx
RUN pipx install poetry
COPY ../pyproject.toml ../poetry.lock /tmp/poetry/
WORKDIR /tmp/poetry
RUN poetry config virtualenvs.create false && poetry install --no-root && rm -rf /tmp/poetry

# install drawio
ENV DRAWIO_VERSION 20.8.16

RUN apt-get install -y wget libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils libatspi2.0-0 libappindicator3-1 libsecret-1-0 libgbm-dev libasound2 xvfb
RUN wget https://github.com/jgraph/drawio-desktop/releases/download/v${DRAWIO_VERSION}/drawio-amd64-${DRAWIO_VERSION}.deb
RUN dpkg --install drawio-amd64-${DRAWIO_VERSION}.deb
RUN rm drawio-amd64-${DRAWIO_VERSION}.deb

RUN apt-get install -y xvfb
RUN echo "#!/bin/sh\nxvfb-run /usr/bin/drawio \"\${@}\"" > /usr/local/bin/drawio && \
    chmod +x /usr/local/bin/drawio