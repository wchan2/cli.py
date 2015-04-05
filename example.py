#!/usr/bin/env python

from cli import App, Flag
import sys
import random

app = App(name='random', description='a random number generator')

@app.command(
    'range',
    'generates random numbers between a specified range',
    [Flag('start', 'the beginning of the range', 0), Flag('end', 'the end of the range', 20)])
def some_command(context):
    print(random.randrange(int(context.get('start')), int(context.get('end'))))


if __name__ == '__main__':
    app.run(sys.argv)