#!/usr/bin/env python

import sys
import random

from cli.app import App
from cli.flag import Flag
from cli.command import Command

app = App(name='random', description='a random number generator')
flags = [Flag('start', 'the beginning of the range', 0), Flag('end', 'the end of the range', 20)]

@app.command(Command('range', 'taking the random number generator', flags))
def some_command(context):
    print(random.randrange(int(context.get('start')), int(context.get('end'))))


if __name__ == '__main__':
    app.run(sys.argv)