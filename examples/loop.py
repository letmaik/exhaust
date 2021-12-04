# This example shows how a space can be modelled with loops.

import exhaust

def generate_numbers(state: exhaust.State):
    numbers = []
    for _ in range(5):
        numbers.append(state.randint(1, 5))
    return numbers

for numbers in exhaust.space(generate_numbers):
    print(numbers)

# Output:
# [1, 1, 1, 1, 1]
# [1, 1, 1, 1, 2]
# [1, 1, 1, 1, 3]
# [1, 1, 1, 1, 4]
# [1, 1, 1, 1, 5]
# [1, 1, 1, 2, 1]
# ...
# [5, 5, 5, 5, 5]
