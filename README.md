
## Command Line Library [![Build Status](https://travis-ci.org/wchan2/cli.py.svg)](https://travis-ci.org/wchan2/cli.py)

A command line library for writing quick command line utilities. 

## Requirements

- Python 3

### TODO:

- Add support to subcommands
- Support for printing help as a subcommand or the `--help` flag
- Support for flags preceded by `--`
- Add to pip
- Add support for different colors to highlight errors better

### Example

The below example builds a range command in `example.py` and can be run via the command:

**Command executed in the command line.**

```
./example.py range -start 1 -end 200
```

**Python example of the range command.**

```python
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
```

## Running the tests

The below command is for running the tests.

```
python setup.py test
```


## License

cli.py is licensed under the [MIT License](http://opensource.org/licenses/MIT).