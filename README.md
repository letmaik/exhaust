# exhaust

A Python library to exhaustively enumerate a combinatorial space represented by a function.

The [API](https://letmaik.github.io/exhaust) is modelled after Python's [`random`](https://docs.python.org/3/library/random.html) module and should feel familiar. An additional convenience function [`maybe()`](https://letmaik.github.io/exhaust/#exhaust.State.maybe) was added to cover a common case.

If you're missing a function and the corresponding space can be enumerated feel free to open an issue. Any functions that generate [real-valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions) cannot be supported.

## Example

```py
import exhaust

def generate_character(state: exhaust.State):
    eyes = []
    for _ in range(state.randint(1, 3)):
        eyes.append({
            'color': state.choice(['brown', 'blue']),
            'glowing': state.maybe()
        })
    size = 'giant' if len(eyes) == 1 else 'normal'
    accessories = []
    if len(eyes) == 2:
        if state.maybe():
            accessories.append('hat')
        if state.maybe():
            accessories.append('ring')    
    character = {
        'size': size,
        'eyes': eyes,
        'accessories': accessories
    }
    return character

# iterates over a space of 132 characters
for character in exhaust.space(generate_character):
    print(character)
```

As you can see, navigating the space works fine within loops as well.
Each time a function from the `State` object is called (like `maybe()`), you can think of it as forking the current path into multiple branches, leading to a tree that gets explored. While exploring, the user-defined function is called for each path of the tree.

See the [examples/](https://github.com/letmaik/exhaust/tree/main/examples) folder for further examples that can be run on the command line.

See the [API Documentation](https://letmaik.github.io/exhaust) for all available `State` functions.

## Installation

```
pip install exhaust
```

## Development

Requires pip >= 21.3

Editable install:
```
pip install -e .
```

Run tests:
```
pip install -r requirements-test.txt
pytest
```

Build docs:
```
pip install -r requirements-docs.txt
sphinx-build -b html docs dist-docs
```

Build wheel:

```
pip install build
python -m build --wheel
```

## Acknowledgments

This package is inspired by [KerasTuner](https://github.com/keras-team/keras-tuner)'s method of defining hyperparameter search spaces.
