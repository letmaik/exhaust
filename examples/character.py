# This example is from the project README.

from pprint import pprint
import exhaust

def generate_character(state: exhaust.State):
    eyes = []
    for _ in range(state.randint(1, 3)):
        eyes.append({
            'color': state.choice(['brown', 'blue']),
            'glowing': state.maybe()
        })
    size = 'giant' if len(eyes) != 2 else 'normal'
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

for character in exhaust.space(generate_character):
    pprint(character, sort_dicts=False)
