from reploncli import reploncli

from datetime import datetime


def cli_function(args):
    print(f"Args entered: {args}")


def prompt():
    return f"{str(datetime.utcnow())} > "


reploncli(cli_function, repl_mode=True, help="<help text>", prompt=prompt)
