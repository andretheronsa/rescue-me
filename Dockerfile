FROM python:3.7.5-alpine

RUN adduser -D rescueme

WORKDIR /home/rescueme

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY wsgi.py config.py entrypoint.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP wsgi.py

RUN chown -R rescueme:rescueme ./
USER rescueme

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]