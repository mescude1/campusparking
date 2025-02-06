# /backend/Dockerfile

FROM python:3.9-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update
RUN apt install libpq-dev python3-dev gcc -y
RUN pip install -r requirements.txt

COPY . .

CMD ["waitress-serve", "--call", "app:create_app"]