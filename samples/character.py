from pprint import pprint
import exhaustive

def generate_character(space: exhaustive.Space):
    eyes = []
    for _ in range(space.randint(1, 3)):
        eyes.append({
            'color': space.choice(['brown', 'blue']),
            'glowing': space.maybe()
        })
    size = 'giant' if len(eyes) != 2 else 'normal'
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

i = 0
for character in exhaustive.iterate(generate_character):
    i += 1
    pprint(character, sort_dicts=False)
print(i)