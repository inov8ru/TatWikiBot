FROM python:3.10

WORKDIR /app

COPY . /app

EXPOSE 80

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["main.py"]