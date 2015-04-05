
## Command Line Library

A command line library for writing quick command line utilities. 

### TODO:

- Add support to subcommands
- Support for printing help as a subcommand or the `--help` flag
- Support for flags preceded by `--`
- Add testing
- Add to pip
- Add support for different colors to highlight errors better

### Example

The below example named `example.py` can be run via the command:

```
./example.py range -start 1 -end 200
```

```python
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
```


## License

cli.py is licensed under the [MIT License](http://opensource.org/licenses/MIT).