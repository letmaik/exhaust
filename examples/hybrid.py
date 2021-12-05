# This example shows how a single function can be used
# for both exhaustive enumeration using this package and
# random sampling using Python's `random` module.

# NOTE: `maybe()` cannot be used because it is not
# available in Python's `random` module. It can be replaced
# with `choice([True, False])` if needed.

import random
import exhaust

def generate_combination(state):
    return {
        'integer': state.randint(1, 3),
        'bool': state.choice([True, False]),
    }

print('Random choice:')
combination = generate_combination(random)
print(combination)
print()

print('Exhaustive choices:')
for combination in exhaust.space(generate_combination):
    print(combination)

# Output:
# Random choice:
# {'integer': 3, 'bool': True}
#
# Exhaustive choices:
# {'integer': 1, 'bool': True}
# {'integer': 1, 'bool': False}
# {'integer': 2, 'bool': True}
# {'integer': 2, 'bool': False}
# {'integer': 3, 'bool': True}
# {'integer': 3, 'bool': False}
