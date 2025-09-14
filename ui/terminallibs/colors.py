class Colors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def green(string):
    return Colors.OK_GREEN + string + Colors.END_C


def red(string):
    return Colors.FAIL + string + Colors.END_C


def yellow(string):
    return Colors.WARNING + string + Colors.END_C


def underline(string):
    return Colors.UNDERLINE + string + Colors.END_C


def blue(string):
    return Colors.OK_BLUE + string + Colors.END_C


def cyan(string):
    return Colors.OK_CYAN + string + Colors.END_C


def bold(string):
    return Colors.BOLD + string + Colors.END_C


def fail(string):
    return Colors.FAIL + string + Colors.END_C


def bold_blue(string):
    return bold(blue(string))


def bold_yellow(string):
    return bold(yellow(string))
