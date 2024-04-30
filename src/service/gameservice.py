import dao.gamedao as dao
from random import randint
from exception import invalidguessexception


def register_new_user(user_name, email):
    return dao.add_player(user_name, email)


def play(secret_id, number):
    if number not in range(1, 10):
        raise invalidguessexception("Guess is not in range")
    return dao.add_result(secret_id, randint(1, 10) == number)


def scoreboard():
    return dao.get_scoreboard()