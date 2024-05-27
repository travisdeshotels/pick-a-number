import os
import requests
from lib.colors import blue, cyan, green, yellow, underline, bold_blue, bold_yellow, fail


class PlayerConfig:
    filename = ".player_config"

    def is_player_configured(self):
        return os.path.isfile(self.filename)

    def load_player_from_config(self):
        with open(self.filename, "r") as config:
            return config.read().split(",")

    def create_config_file(self):
        with open(self.filename, "w") as config:
            url = input("Enter host url: ")
            secret_id = input("Enter your secret_id: ")
            config.write(f"{url},{secret_id}")
            return url, secret_id

    def get_config_values(self):
        if self.is_player_configured():
            return self.load_player_from_config()
        else:
            return self.create_config_file()


def print_result(result):
    print(f"\nNumber is {blue(str(result['correctNumber']))}")
    print(green("You win!") if result['result'] == 'win'
          else f"You lost with a guess of {fail(str(result['guess']))}")
    print()


def print_stats(stats):
    print(underline('Your stats'))
    print(f"wins: {green(str(stats['wins']))}")
    print(f"most guessed: {yellow(str(stats['mostGuessed']))}")
    print(f"total guesses: {bold_blue(str(stats['total']))}")
    print()


class PlayHelper:
    def __init__(self):
        if os.environ.get('GAME_URL') and os.environ.get('SECRET_ID'):
            self.game_url = os.environ['GAME_URL']
            self.secret_id = os.environ['SECRET_ID']
        else:
            self.game_url, self.secret_id = PlayerConfig().get_config_values()

    def play(self):
        guess = int(input('Enter a number between 1 and 10: '))
        while guess not in range(1, 11):
            print('Bad input. Try again.')
            guess = int(input('Enter a number between 1 and 10: '))
        data = requests.get(headers={'Secret': self.secret_id}, url=f'{self.game_url}/?guess={guess}').json()
        print_result(data['result'])
        print_stats(data['stats'])

    def scoreboard(self):
        scores = requests.get(f'{self.game_url}/scores').json()
        print(underline('\nHigh scores:'))
        for score in scores:
            print(blue(score['player']) + ': ' + cyan(str(score['score'])))
        print()


play_helper = PlayHelper()
prompt = f'({bold_yellow("p")})lay\n({bold_yellow("s")})coreboard\n({bold_yellow("q")})uit\n'
choice = input(prompt)
while choice != 'q':
    if choice == 's':
        play_helper.scoreboard()
    elif choice == 'p':
        play_helper.play()
    choice = input(prompt)
