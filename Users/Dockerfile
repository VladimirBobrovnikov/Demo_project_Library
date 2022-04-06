#1. Спульте приложение из репозитория
#2. Упакуйте приложение в докер контейнер.
#3. Для базы PostgreSQL спульте образ и запустите докер контейнер.
#4. Настройте приложение на базу в другом контейнере.
#5. Запустите приложение и проверьте работоспособность приложения.

FROM python:3.7

#ENV USER=postgres
#ENV PASSWORD=password
#ENV HOST=postgres-test2
#ENV PORT=5432
#ENV DATABASE=test

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "run.py"]

#docker run --name postgres-test2 -e POSTGRES_PASSWORD="password" -e POSTGRES_USER="po
#stgres" -e POSTGRES_DB="test" -p 5432:5432 --rm --network skynet -d postgres

#docker run --name task2 --network skynet -p 8080:1234 --rm -it task2-test
