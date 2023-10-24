FROM python:3.10.13-alpine3.18

WORKDIR /app

RUN pip3 install aiogram python-dotenv mysql-connector-python

COPY . .

CMD ["python", "main.py"]