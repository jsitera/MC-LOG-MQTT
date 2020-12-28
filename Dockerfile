FROM python:3

#RUN apt-get update

COPY README.docker.md /
COPY README.md /
CMD mkdir /workdir
WORKDIR /workdir

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY mc-log-mqtt.py /workdir
COPY config.py /workdir

# shared data of minecraft server
VOLUME ["/data"]

ENTRYPOINT ["python3", "/workdir/mc-log-mqtt.py"]
