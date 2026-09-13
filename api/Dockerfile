FROM astral/uv:python3.14-bookworm-slim

WORKDIR /app

COPY pyproject.toml ./

COPY src /app
COPY db /app/db

RUN python3 db/initdb.py game.db
RUN mv game.db db/game.db
ENV SQLITE_DB=/app/db/game.db

EXPOSE 8000

CMD [ "uv", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]
