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
