# /backend/Dockerfile

FROM python:3.9-bookworm

WORKDIR /Backend

COPY requirements.txt requirements.txt
RUN apt update
RUN apt install libpq-dev python3-dev gcc -y
RUN pip install -r requirements.txt
RUN pip install flask-login

COPY . .

CMD ["flask", "db", "migrate"]