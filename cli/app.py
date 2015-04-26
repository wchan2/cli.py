import sys
from collections import defaultdict
from cli.context import Context
import argparse

class App:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.commands = []
        
    def command(self, command):
        self.commands.append(command)
        return self.commands[-1]

    def run(self, argv):
        if len(argv) < 2 or not self._find_command(argv[1]):
            self.print_help()
            sys.exit(1)

        command = self._find_command(argv[1])
        command.execute(self._create_context(command, argv))

    def create_parser(self, command):
        parser = argparse.ArgumentParser(prog=self.name, description=self.description)
        parser.add_argument(command.name, help=command.description)

        for flag in command.flags:
            parser.add_argument(''.join(['-', flag.name]), ''.join(['--', flag.name]), default=flag.default, help=flag.description)
        return parser

    def print_help(self):
        for command in self.commands:
            self.create_parser(command).print_help()

    def _find_command(self, cmd_name):
        found_commands = list(filter(lambda cmd: cmd.name == cmd_name, self.commands))
        if len(found_commands) == 1:
            return found_commands[0]
        return None

    def _create_context(self, command, argv):
        context = Context()
        cli_args = self.create_parser(command).parse_args(argv[1:])
        for flag in command.flags:
            context.set(flag.name, getattr(cli_args, flag.name))
        return context