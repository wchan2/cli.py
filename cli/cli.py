import sys
from collections import defaultdict

class App:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.commands = []
    def command(self, name, description, flags=[]):
        self.commands.append(Command(name, description, flags))
        return self.commands[-1:][0]
    def print_help(self):
        print('\n'.join(map(lambda cmd: str(cmd), self.commands)))
    def run(self, cli_args):
        if len(cli_args) < 2:
            self.print_help()
            sys.exit(1)
        command = self._find_command(cli_args[1])
        if not command:
            self.print_help()
            sys.exit(1)    
        arguments = self._build_arguments(cli_args)
        context = self._build_context(command.flags, arguments)
        command.execute(context)
    def _find_command(self, cmd_name):
        found_commands = filter(lambda cmd: cmd.name == cmd_name, self.commands)
        if len(found_commands) == 1:
            return found_commands[0]
        return None
    def _build_arguments(self, cli_args):
        arguments = defaultdict(lambda: None)
        for i, arg in enumerate(cli_args):
            if arg.startswith('-'):
                try:
                    arguments[arg.replace('-', '')] = cli_args[i + 1]
                except:
                    print('%s flag specified without a value\n--' % arg.replace('-', ''))
                    self.print_help()
                    sys.exit(1)
        return arguments
    def _build_context(self, flags, arguments):
        context = Context()
        for flag in flags:
            if arguments[flag.name]:
                context.set(flag.name, arguments[flag.name])
            else:
                context.set(flag.name, flag.value)
        return context

class Command:
    def __init__(self, name, description, flags=[]):
        self.name = name
        self.flags = flags
        self.description = description
    def execute(self, context):
        self.action(context)
    def __call__(self, fn):
        self.action = fn
    def __repr__(self):
        help_text = ['name: %s' % self.name]
        if self.description != None:
            help_text.append('description: %s' % (self.description, ))
        flag_strings = map(lambda flag: str(flag), self.flags)
        help_text.append('flags:')
        help_text.append('\n'.join(flag_strings))
        return '\n'.join(help_text)

class Flag:
    def __init__(self, name, description, value=None):
        self.name = name
        self.description = description
        self.value = value
    def __repr__(self):
        return ' - %s: %s' % (self.name, self.description)

class Context:
    def __init__(self):
        self.values = defaultdict(lambda: None)
    def set(self, key, value):
        self.values[key] = value
    def get(self, key):
        return self.values[key]