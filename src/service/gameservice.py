import dao.gamedao as dao
from random import randint

from exception.invalidguessexception import InvalidGuessException


def register_new_user(user_name, email):
    return dao.add_player(user_name, email)


def play(secret_id, number):
    if number not in range(1, 11):
        raise InvalidGuessException("Guess is not in range")
    correct_number = randint(1, 10)
    result = dao.add_result(secret_id, correct_number == number)
    result['guess'] = number
    result['correct_number'] = correct_number
    result['result'] = 'win' if correct_number == number else 'lose'
    return result


def scoreboard():
    return dao.get_scoreboard()