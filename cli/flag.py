
class Flag:
    def __init__(self, name, description, default=None):
        self.name = name
        self.description = description
        self.default = default

    def __repr__(self):
        return ' - %s: %s' % (self.name, self.description)