FROM python:3.10-alpine

RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /hello_world

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]