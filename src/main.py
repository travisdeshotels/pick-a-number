from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Annotated

import service.gameservice as service

app = FastAPI()


class GameUser(BaseModel):
    userName: str
    email: str


@app.post("/register")
def register(game_user: GameUser):
    secret_id = service.register_new_user(game_user.userName, game_user.email)
    return {
        "message": "Registration complete. Use secret_id to play.",
        "secretId": secret_id
    }


@app.get("/")
def play(secret: Annotated[str | None, Header()] = None, guess: int = 11):
    return service.play(secret, guess)


@app.get("/scores")
def get_scores():
    return service.scoreboard()
