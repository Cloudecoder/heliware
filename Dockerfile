# syntax=docker/dockerfile:1
FROM ubuntu:20.04
ENV DOCKER_BUILDKIT=1
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app
RUN  apt-get update \
    && apt-get install python3-pip -y
RUN apt-get install gdal-bin -y \
    && apt-get install libgdal-dev -y
RUN pip3 install -r requirements.txt
COPY . .
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

COPY . /app
ENTRYPOINT [ "python3" ]
CMD ["app.py"]
