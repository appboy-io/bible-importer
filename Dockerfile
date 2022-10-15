FROM python:3.9.6-alpine3.14
ADD . /code
WORKDIR /code
RUN apk update
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps
RUN apk add git
RUN pip install -r requirements.txt
CMD ["python", "main.py"]