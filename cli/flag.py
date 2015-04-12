
class Flag:
    def __init__(self, name, description, value=None):
        self.name = name
        self.description = description
        self.value = value
        
    def __repr__(self):
        return ' - %s: %s' % (self.name, self.description)