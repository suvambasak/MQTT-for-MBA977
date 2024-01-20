FROM python:3.11.7-alpine3.19
WORKDIR /usr/src/app
COPY ./index.html .
CMD [ "python3", "-m", "http.server", "8000" ]