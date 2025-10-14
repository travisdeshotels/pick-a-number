import dao.gamedao as dao
from random import randint

from exception.invalidguessexception import InvalidGuessException
from exception.baddataexception import BadDataException
import util.loggingutil as log

def register_new_user(user_name, email):
    return dao.add_player(user_name, email)


def play(secret_id, guess):
    if guess not in range(1, 11):
        raise InvalidGuessException("Guess is not in range")
    correct_number = randint(1, 10)
    result = dao.add_play_result(secret_id, guess, correct_number == guess)
    if result is None:
        raise BadDataException('Unable to save play data! Bad data was provided.')
    result['result'] = {}
    result['result']['guess'] = guess
    result['result']['correctNumber'] = correct_number
    result['result']['result'] = 'win' if correct_number == guess else 'lose'
    log.logger.debug(f'Player {dao.get_player_info_by_secret_id(secret_id)["username"]} '
                     f'Result guess {result["result"]["guess"]} correct {result["result"]["correctNumber"]} '
                     f'{result["result"]["result"]}')

    return result


def scoreboard():
    result = []
    score_data = dao.get_scoreboard()
    for score_datum in score_data:
        result.append(
            {
                "player": score_datum[0],
                "score": score_datum[1]
            }
        )
    return result
