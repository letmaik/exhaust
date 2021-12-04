import exhaustive

def generate_computer(space: exhaustive.Space):
    has_dedicated_gpu = space.maybe()
    if has_dedicated_gpu:
        gpu_vendor = space.choice(["nvidia", "amd"])
    else:
        gpu_vendor = "intel"
    return {
        "dedicated_gpu": has_dedicated_gpu,
        "gpu_vendor": gpu_vendor
    }

for computer in exhaustive.iterate(generate_computer):
    print(computer)

# Output:
# {'dedicated_gpu': True, 'gpu_vendor': 'nvidia'}
# {'dedicated_gpu': True, 'gpu_vendor': 'amd'}
# {'dedicated_gpu': False, 'gpu_vendor': 'intel'}
