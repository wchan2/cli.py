from collections import defaultdict

class Context:
    def __init__(self):
        self.values = defaultdict(lambda: None)

    def set(self, key, value):
        self.values[key] = value
        
    def get(self, key):
        return self.values[key]