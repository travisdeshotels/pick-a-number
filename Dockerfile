FROM python:3.11-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src /app
COPY db /app/db

RUN python3 db/initdb.py game.db
RUN mv game.db db/game.db
ENV SQLITE_DB=/app/db/game.db

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]
