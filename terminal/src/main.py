import os
import requests
from lib.colors import blue, cyan, green, yellow, underline, bold, bold_blue, bold_yellow, fail

game_url = os.environ['GAME_URL']
secret_id = os.environ['SECRET_ID']


def play():
    # data = {'username': 'me',
    #         'stats': {'total': 21, 'wins': 1, 'mostGuessed': 3},
    #         'result': {'guess': 4, 'correctNumber': 8, 'result': 'loss'}}
    guess = int(input('Enter a number between 1 and 10: '))
    while guess not in range(1, 11):
        print('Bad input. Try again.')
        guess = int(input('Enter a number between 1 and 10: '))
    data = requests.get(headers={'Secret': secret_id}, url=f'{game_url}/?guess={guess}').json()

    print(f"\nNumber is {blue(str(data['result']['correctNumber']))}")
    print(green("You win!") if data['result']['result'] == 'win'
          else f"You lost with a guess of {fail(str(data['result']['guess']))}")
    print()
    print(underline('Your stats'))
    print(f"wins: {green(str(data['stats']['wins']))}")
    print(f"most guessed: {yellow(str(data['stats']['mostGuessed']))}")
    print(f"total guesses: {bold_blue(str(data['stats']['total']))}")
    print()


def scoreboard():
    # scores = [{'player': 'me', 'score': 1},
    #           {'player': 'you', 'score': 2}]
    scores = requests.get(f'{game_url}/scores').json()
    print(underline('\nHigh scores:'))
    for score in scores:
        print(blue(score['player']) + ': ' + cyan(str(score['score'])))
    print()


prompt = f'({bold_yellow("p")})lay\n({bold_yellow("s")})coreboard\n({bold_yellow("q")})uit\n'
choice = input(prompt)
while choice != 'q':
    if choice == 's':
        scoreboard()
    elif choice == 'p':
        play()
    choice = input(prompt)
