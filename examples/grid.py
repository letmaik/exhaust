# This example shows how to iterate over a grid of parameters.

import exhaust

def generate_combination(state: exhaust.State):
    return {
        'integer': state.randint(1, 5),
        'bool': state.maybe(),
        'choice': state.choice([1, None, 'foo', ['bar']])
    }

for combination in exhaust.space(generate_combination):
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
