import exhaust

products = {}

def multiply(state: exhaust.State):
    i = state.randint(1, 10)
    j = state.randint(1, 10)
    products[(i, j)] = i * j

for _ in exhaust.space(multiply):
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
