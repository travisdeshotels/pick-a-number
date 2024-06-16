import os
import requests
from colors import blue, cyan, green, yellow, underline, bold_blue, fail
from playerconfig import PlayerConfig


def print_result(result):
    print(f"\nNumber is {blue(str(result['correctNumber']))}")
    print(green("You win!") if result['result'] == 'win'
          else f"You lost with a guess of {fail(str(result['guess']))}")
    print()


def print_stats(stats, username):
    print(underline(f'{username} stats'))
    print(f"wins: {green(str(stats['wins']))}")
    print(f"most guessed: {yellow(str(stats['mostGuessed']))}")
    print(f"total guesses: {bold_blue(str(stats['total']))}")
    print()


class PlayHelper:
    def __init__(self, filename):
        if os.environ.get('GAME_URL') and os.environ.get('SECRET_ID'):
            self.game_url = os.environ['GAME_URL']
            self.secret_id = os.environ['SECRET_ID']
        else:
            self.game_url, self.secret_id = PlayerConfig(filename).get_config_values()

    def play(self):
        guess = int(input('Enter a number between 1 and 10: '))
        while guess not in range(1, 11):
            print('Bad input. Try again.')
            guess = int(input('Enter a number between 1 and 10: '))
        data = requests.get(headers={'Secret': self.secret_id}, url=f'{self.game_url}/?guess={guess}').json()
        print_result(data['result'])
        print_stats(data['stats'], data['username'])

    def scoreboard(self):
        scores = requests.get(f'{self.game_url}/scores').json()
        print(underline('\nHigh scores:'))
        for score in scores:
            print(blue(score['player']) + ': ' + cyan(str(score['score'])))
        print()
