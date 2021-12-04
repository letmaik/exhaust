# This example shows how conditions can be used to model dependencies.

import exhaust

def generate_computer(state: exhaust.State):
    has_dedicated_gpu = state.maybe()
    if has_dedicated_gpu:
        gpu_vendor = state.choice(["nvidia", "amd"])
    else:
        gpu_vendor = "intel"
    return {
        "dedicated_gpu": has_dedicated_gpu,
        "gpu_vendor": gpu_vendor
    }

for computer in exhaust.space(generate_computer):
    print(computer)

# Output:
# {'dedicated_gpu': True, 'gpu_vendor': 'nvidia'}
# {'dedicated_gpu': True, 'gpu_vendor': 'amd'}
# {'dedicated_gpu': False, 'gpu_vendor': 'intel'}
