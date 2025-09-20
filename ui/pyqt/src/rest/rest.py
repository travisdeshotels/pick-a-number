import requests

class RestCaller:
    api_url = ""
    secret_id = ""

    def __init__(self, config_tuple):
        self.api_url = config_tuple[0]
        self.secret_id = config_tuple[1]

    def submit_guess(self, guess):
        return requests.get(headers={'Secret': self.secret_id}, url=f'{self.api_url}?guess={guess}').json()


def print_result(result):
    print(f"\nNumber is {str(result['correctNumber'])}")
    print("You win!" if result['result'] == 'win'
          else f"You lost with a guess of {str(result['guess'])}")
    print()


def print_stats(stats, username):
    print(f'{username} stats')
    print(f"wins: {str(stats['wins'])}")
    print(f"most guessed: {str(stats['mostGuessed'])}")
    print(f"total guesses: {str(stats['total'])}")
    print()
