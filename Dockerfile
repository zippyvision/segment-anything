# syntax=docker/dockerfile:1

FROM nvcr.io/nvidia/pytorch:23.07-py3

RUN python -m pip install --upgrade pip

WORKDIR /app
