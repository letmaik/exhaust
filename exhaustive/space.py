class SpaceExhausted(Exception):
    pass

class Space:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.stack_values = []
        self.stack_labels = []
        self.loc = -1
        self.exhausted = False

    def rewind(self):
        self.loc = -1
        self.stack_labels.clear()

    def choice(self, seq, label=None):
        if self.exhausted:
            raise SpaceExhausted()
        top = len(self.stack_values) - 1
        self.loc += 1
        if self.verbose:
            print(f'loc={self.loc}')
        if self.loc > top:
            # Enter a new branch.
            seq = list(seq)
            assert len(seq) > 0
            self.stack_values.append(seq)
        else:
            # Check if rest of stack has been exhausted.
            is_exhausted = True
            for loc in range(self.loc + 1, top + 1):
                if len(self.stack_values[loc]) > 1:
                    is_exhausted = False
                    break
            # If so, pop the stack and continue with the next branch if any.
            # Otherwise, continue with the current branch.
            if is_exhausted:
                self.stack_values = self.stack_values[:self.loc+1]
                self.stack_values[self.loc].pop(0)
                if len(self.stack_values[self.loc]) == 0:
                    if self.verbose:
                        print(f'Space exhausted')
                    self.exhausted = True
                    raise SpaceExhausted()
                else:
                    if self.verbose:
                        print(f'Branch exhausted')
        value = self.stack_values[self.loc][0]
        if callable(label):
            label = label(value)
        self.stack_labels.append(label)
        if self.verbose:
            print(f'Label: {label}')
            print(f'Value: {value}')
            print(f'Stack:')
            for loc, branch in enumerate(self.stack_values):
                print(f'  {loc}: {branch}')
        return value

    def maybe(self, label=None):
        return self.choice([True, False], label=label)
        
    def randint(self, start, end, label=None):
        return self.choice(range(start, end + 1), label=label)

def iterate(fn, return_labels=False, verbose=False):
    space = Space(verbose=verbose)
    try:
        while True:
            space.rewind()
            result = fn(space)
            if return_labels:
                labels = [label for label in space.stack_labels
                          if label is not None]
                yield result, labels
            else:
                yield result
    except SpaceExhausted:
        pass
