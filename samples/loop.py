import exhaustive

def generate_numbers(space: exhaustive.Space):
    numbers = []
    for _ in range(5):
        numbers.append(space.randint(1, 5))
    return numbers

for numbers in exhaustive.iterate(generate_numbers):
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
