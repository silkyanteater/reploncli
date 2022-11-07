from reploncli import reploncli

from datetime import datetime


def cli_function(args):
    print(f"Args entered: {args}")
    if len(args) == 1 and args[0].lower() in ('exit', 'quit'):
        return True


def prompt():
    return f"{str(datetime.utcnow())} > "


reploncli(cli_function, repl_mode=True, help="<help text>", prompt=prompt)
