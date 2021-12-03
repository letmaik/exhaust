# exhaustive

A Python library to exhaustively and dynamically iterate a search space.

The API is modelled after Python's [`random`](https://docs.python.org/3/library/random.html) module and should feel familiar. Some additional convenience functions were added to cover common cases, like `maybe()`.

If you're missing a function and the corresponding space can be iterated feel free to open an issue. Any functions that generate [real-valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions) cannot be supported.

## Example

```py
import exhaustive

def generate_character(space: exhaustive.Space):
    eyes = []
    for _ in range(space.randint(1, 3)):
        eyes.append({
            'color': space.choice(['brown', 'blue']),
            'glowing': space.maybe()
        })
    size = 'giant' if len(eyes) == 1 else 'normal'
    accessories = []
    if len(eyes) == 2:
        if space.maybe():
            accessories.append('hat')
        if space.maybe():
            accessories.append('ring')    
    character = {
        'size': size,
        'eyes': eyes,
        'accessories': accessories
    }
    return character

# iterates over a space of 132 items
for character in exhaustive.iterate(generate_character):
    print(character)
```

As you can see, navigating the search space works fine within loops as well.
Each time a function from the `Space` object is called (like `maybe()`), you can think of it as forking the current path into multiple branches, leading to a tree that gets explored. While exploring, the user-defined function is called for each path of the tree.

## Install

```
pip install exhaustive
```

## Samples

See the [samples/](samples) folder for scripts that can be run on the command line.

## Development

Requires pip >= 21.3

```
pip install -e .[test]
pytest
```

## Acknowledgments

This package is inspired by [KerasTuner](https://github.com/keras-team/keras-tuner)'s method of defining hyperparameter search spaces.
