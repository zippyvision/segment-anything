# syntax=docker/dockerfile:1

FROM nvcr.io/nvidia/pytorch:23.07-py3

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN python -m pip install -e .
RUN python -m pip install pycocotools matplotlib onnxruntime onnx
