FROM python:3.6-alpine

RUN [ "pip3", "install", "requests" ]

COPY src /usr/src/app/
WORKDIR /usr/src/app
CMD [ "python", "-m", "unittest" ]
