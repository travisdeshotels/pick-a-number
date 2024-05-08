import dao.gamedao as dao
from random import randint

from exception.invalidguessexception import InvalidGuessException


def register_new_user(user_name, email):
    return dao.add_player(user_name, email)


def play(secret_id, guess):
    if guess not in range(1, 11):
        raise InvalidGuessException("Guess is not in range")
    correct_number = randint(1, 10)
    result = dao.add_play_result(secret_id, guess, correct_number == guess)
    result['result'] = {}
    result['result']['guess'] = guess
    result['result']['correctNumber'] = correct_number
    result['result']['result'] = 'win' if correct_number == guess else 'lose'
    return result


def scoreboard():
    return dao.get_scoreboard()
