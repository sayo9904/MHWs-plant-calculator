FROM python:3.12-slim

RUN apt update && apt install -y \
    locales \
    git\
    sudo \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i -e 's/# \(ja_JP.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen \
    && update-locale
ENV LANG=ja_JP.UTF-8

ENV TZ=Asia/Tokyo

RUN useradd -m python && usermod -aG sudo python
USER python

ENV PYTHONPATH=/workspaces/MHWs-plant-calclator/src
