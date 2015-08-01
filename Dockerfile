FROM alpine

RUN apk add --update python python-dev uwsgi uwsgi-python py-pip

RUN pip install -U pip virtualenv

ADD requirements.txt /config/requirements.txt

RUN virtualenv /venv && \
    . /venv/bin/activate && \
    pip install -r /config/requirements.txt

ADD assets /built/static
ADD assets /app/static

ADD config /config
ADD static_server /app

CMD uwsgi --yaml config/uwsgi.yml 
