import exhaustive

def generate_combination(space: exhaustive.Space):
    return {
        'integer': space.randint(1, 5),
        'bool': space.maybe(),
        'choice': space.choice([1, None, 'foo', ['bar']])
    }

for combination in exhaustive.iterate(generate_combination):
    print(combination)

# Output:
# {'integer': 1, 'bool': True, 'choice': 1}
# {'integer': 1, 'bool': True, 'choice': None}
# {'integer': 1, 'bool': True, 'choice': 'foo'}
# {'integer': 1, 'bool': True, 'choice': ['bar']}
# {'integer': 1, 'bool': False, 'choice': 1}
# {'integer': 1, 'bool': False, 'choice': None}
# {'integer': 1, 'bool': False, 'choice': 'foo'}
# {'integer': 1, 'bool': False, 'choice': ['bar']}
# {'integer': 2, 'bool': True, 'choice': 1}
# ...
