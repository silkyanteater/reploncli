from reploncli import reploncli

from datetime import datetime


SYS_COMMAND_PREFIX = "."

HELP_TEXT = f"help: this message / exit: exit / {SYS_COMMAND_PREFIX}<command>: system command"


def cli_function(args):
    if len(args) == 1 and args[0].lower() in ('?', 'h'):
        print(HELP_TEXT)
        return
    if len(args) == 1 and args[0].lower() in ('x', 'exit', 'q', 'quit'):
        return True
    print(f"Args entered: {args}")


def prompt():
    return f"{str(datetime.utcnow())} > "


reploncli(cli_function, repl_mode=True, help=HELP_TEXT, prompt=prompt, sys_command_prefix=SYS_COMMAND_PREFIX)
