FROM python:3.10
LABEL maintainer = "Pablo de Andrades Lima"


RUN apt-get update
COPY ./requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
RUN export FLASK_APP=app.py

WORKDIR /
COPY ./ /

CMD [ "flask",  "run", "--host=0.0.0.0",  "--port=8080" ]