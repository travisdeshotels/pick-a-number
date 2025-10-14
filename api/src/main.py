from fastapi import FastAPI, Header, Response, status
from pydantic import BaseModel
from typing import Annotated
from exception.invalidguessexception import InvalidGuessException
from exception.baddataexception import BadDataException

import service.gameservice as service
import util.loggingutil as log

app = FastAPI()

class GameUser(BaseModel):
    userName: str
    email: str


@app.post("/register", status_code=201)
def register(game_user: GameUser, response: Response):
    secret_id = service.register_new_user(game_user.userName, game_user.email)
    if secret_id:
        log.logger.info(f'User just registered username {game_user.userName} email {game_user.email}')
        return {
            "message": "Registration complete. Use secret_id to play.",
            "secretId": secret_id
        }
    else:
        log.logger.error(f'Error occurred during registration username {game_user.userName} email {game_user.email}')
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "Bad request."
        }


@app.get("/", status_code=200)
def play(response: Response, secret: Annotated[str | None, Header()] = None, guess: int = 11):
    try:
        if secret is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            log.logger.debug("User attempted to play without using a secret id")
            return {"message": "Missing secret id."}
        return service.play(secret, guess)
    except BadDataException:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "Bad request."
        }
    except InvalidGuessException:
        return {
            "message": "Guess a number between 1 and 10."
        }


@app.get("/scores", status_code=200)
def get_scores():
    return service.scoreboard()
