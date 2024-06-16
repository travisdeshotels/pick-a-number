from terminallibs.colors import bold_yellow
from lib.playhelper import PlayHelper


play_helper = PlayHelper('.player_config')
prompt = f'({bold_yellow("p")})lay\n({bold_yellow("s")})coreboard\n({bold_yellow("q")})uit\n% '
choice = input(prompt)
while choice != 'q':
    if choice == 's':
        play_helper.scoreboard()
    elif choice == 'p':
        play_helper.play()
    choice = input(prompt)
