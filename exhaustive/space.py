class SpaceExhausted(Exception):
    pass

class Space:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.stack = []
        self.loc = -1
        self.exhausted = False

    def rewind(self):
        self.loc = -1

    def choice(self, seq, name=None):
        if self.exhausted:
            raise SpaceExhausted()
        if self.verbose and name is None:
            name = '<unnamed>'
        top = len(self.stack) - 1
        self.loc += 1
        if self.verbose:
            print(f'loc={self.loc}')
        if self.loc > top:
            # Enter a new branch.
            seq = list(seq)
            assert len(seq) > 0
            self.stack.append(seq)
        else:
            # Check if rest of stack has been exhausted.
            is_exhausted = True
            for loc in range(self.loc + 1, top + 1):
                if len(self.stack[loc]) > 1:
                    is_exhausted = False
                    break
            # If so, pop the stack and continue with the next branch if any.
            # Otherwise, continue with the current branch.
            if is_exhausted:
                self.stack = self.stack[:self.loc+1]
                self.stack[self.loc].pop(0)
                if len(self.stack[self.loc]) == 0:
                    if self.verbose:
                        print(f'Space exhausted')
                    self.exhausted = True
                    raise SpaceExhausted()
                else:
                    if self.verbose:
                        print(f'Branch exhausted')
        value = self.stack[self.loc][0]
        if self.verbose:
            print(f'{name}={value}')
            print(f'Stack:')
            for loc, branch in enumerate(self.stack):
                print(f'  {loc}: {branch}')
        return value

    def maybe(self, name=None):
        return self.choice([True, False], name=name)
        
    def randint(self, start, end, name=None):
        return self.choice(range(start, end + 1), name=name)

def iterate(fn, verbose=False):
    space = Space(verbose=verbose)
    try:
        while True:
            space.rewind()
            yield fn(space)
    except SpaceExhausted:
        pass
