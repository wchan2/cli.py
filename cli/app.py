import sys
from collections import defaultdict

class App:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.commands = []
        
    def command(self, command):
        self.commands.append(command)
        return self.commands[-1]

    def print_help(self):
        print('\n'.join(map(lambda cmd: str(cmd), self.commands)))

    def run(self, cli_args):
        if len(cli_args) < 2:
            print('command name required')
            self.print_help()
            sys.exit(1)
        command = self._find_command(cli_args[1])
        if not command:
            self.print_help()
            sys.exit(1)
        command.execute(cli_args)

    def _find_command(self, cmd_name):
        found_commands = list(filter(lambda cmd: cmd.name == cmd_name, self.commands))
        if len(found_commands) == 1:
            return found_commands[0]
        return None