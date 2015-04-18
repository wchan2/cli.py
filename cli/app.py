import sys
from collections import defaultdict
from cli.context import Context

class App:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.commands = []
        
    def command(self, command):
        self.commands.append(command)
        return self.commands[-1]

    def run(self, cli_args):
        if len(cli_args) < 2:
            self._print_command_name_required()
            self.print_help()
            sys.exit(1)
        command = self._find_command(cli_args[1])
        if not command:
            self.print_help()
            sys.exit(1)
        args = self._parse_arguments(cli_args)
        context = self._parse_context(command.flags, args)
        command.execute(context)

    def print_help(self):
        print('\n'.join(map(lambda cmd: str(cmd), self.commands)))

    def _print_command_name_required(self):
        print('command name required')

    def _print_flag_value_required(self, flag):
        print('%s flag specified without a value\n--' % flag.replace('-', ''))

    def _find_command(self, cmd_name):
        found_commands = list(filter(lambda cmd: cmd.name == cmd_name, self.commands))
        if len(found_commands) == 1:
            return found_commands[0]
        return None

    def _parse_context(self, flags, cli_arguments):
        context = Context()
        for flag in flags:
            if cli_arguments[flag.name]:
                context.set(flag.name, cli_arguments[flag.name])
            else:
                context.set(flag.name, flag.value)
        return context

    def _parse_arguments(self, cli_arguments):
        arguments = defaultdict(lambda: None)
        for i, arg in enumerate(cli_arguments):
            if arg.startswith('-'):
                try:
                    arguments[arg.replace('-', '')] = cli_arguments[i + 1]
                except:
                    self._print_flag_value_required()
                    self.print_help()
                    sys.exit(1)
        return arguments