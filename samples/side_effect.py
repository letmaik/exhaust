import exhaustive

products = {}

def multiply(space: exhaustive.Space):
    i = space.randint(1, 10)
    j = space.randint(1, 10)
    products[(i, j)] = i * j

for _ in exhaustive.iterate(multiply):
    pass

for i in range(1, 11):
    print(products[(i,i)])

# Output:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
