from collections import defaultdict
from cli.context import Context

class Command:
    def __init__(self, name, description, flags=[]):
        self.name = name
        self.flags = flags
        self.description = description
        
    def execute(self, cli_arguments):
        arguments = self._parse_arguments(cli_arguments)
        context = self.parse_context(arguments)
        self.action(context)

    def parse_context(self, cli_arguments):
        context = Context()
        for flag in self.flags:
            if cli_arguments[flag.name]:
                context.set(flag.name, cli_arguments[flag.name])
            else:
                context.set(flag.name, flag.value)
        return context

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

    def _parse_arguments(self, cli_arguments):
        arguments = defaultdict(lambda: None)
        for i, arg in enumerate(cli_arguments):
            if arg.startswith('-'):
                try:
                    arguments[arg.replace('-', '')] = cli_arguments[i + 1]
                except:
                    print('%s flag specified without a value\n--' % arg.replace('-', ''))
                    self.print_help()
                    sys.exit(1)
        return arguments