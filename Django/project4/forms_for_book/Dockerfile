FROM python:3.10-slim

RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /forms_for_book

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# информирует пользователя, какой порт внутри контейнера работает
EXPOSE 8080

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]