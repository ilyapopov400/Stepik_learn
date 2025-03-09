FROM python:3.10-slim

# создание новой группы и пользователя в ней
RUN groupadd -r newgroup && useradd -r -g newgroup user1

RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /hello_world

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# информирует пользователя, какой порт внутри контейнера работает
EXPOSE 8080

# переходим в пользователя user1
USER user1

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]