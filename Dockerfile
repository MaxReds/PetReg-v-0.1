FROM python:3.8

COPY . /app
WORKDIR /app

CMD ["python", "petreg.py"]


