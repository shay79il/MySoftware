FROM python:3.8.3-alpine

RUN adduser -D app
USER app

WORKDIR /home/app

COPY --chown=app:app main.py /home/app/

CMD [ "python", "/home/app/main.py" ]