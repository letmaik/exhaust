"The exhaust package"

__version__ = "0.1.0"

class SpaceExhausted(Exception):
    pass

class State:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self._stack = []
        self._loc = -1
        self._exhausted = False

    def _rewind(self):
        self._loc = -1

    def choice(self, seq):
        if self._exhausted:
            raise SpaceExhausted()
        top = len(self._stack) - 1
        self._loc += 1
        if self.verbose:
            print(f'loc={self._loc}')
        if self._loc > top:
            # Enter a new branch.
            seq = list(seq)
            if len(seq) == 0:
                raise ValueError('Empty sequence')
            self._stack.append(seq)
        else:
            # Check if rest of stack has been exhausted.
            is_exhausted = True
            for loc in range(self._loc + 1, top + 1):
                if len(self._stack[loc]) > 1:
                    is_exhausted = False
                    break
            # If so, pop the stack and continue with the next branch if any.
            # Otherwise, continue with the current branch.
            if is_exhausted:
                self._stack = self._stack[:self._loc+1]
                self._stack[self._loc].pop(0)
                if len(self._stack[self._loc]) == 0:
                    if self.verbose:
                        print(f'Space exhausted')
                    self._exhausted = True
                    raise SpaceExhausted()
                else:
                    if self.verbose:
                        print(f'Branch exhausted')
        value = self._stack[self._loc][0]
        if self.verbose:
            print(f'Value: {value}')
            print(f'Stack:')
            for loc, branch in enumerate(self._stack):
                print(f'  {loc}: {branch}')
        return value

    def maybe(self):
        return self.choice([True, False])
        
    def randint(self, start, end):
        return self.choice(range(start, end + 1))


class SpaceIterable:
    def __init__(self, fn, verbose=False):
        self.fn = fn
        self.verbose = verbose

    def __iter__(self):
        state = State(verbose=self.verbose)
        try:
            while True:
                state._rewind()
                yield self.fn(state)
        except SpaceExhausted:
            pass


def space(fn, verbose=False):
    return SpaceIterable(fn, verbose=verbose)
