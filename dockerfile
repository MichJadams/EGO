FROM python:3.7-alpine

COPY requirements.txt /

USER root

RUN pip install -r /requirements.txt

COPY src/ /src
COPY execute.sh /src

WORKDIR /src

ENTRYPOINT ["sh","/src/execute.sh"]
