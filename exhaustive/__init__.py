"The exhaustive package"

__version__ = "0.1.0"

class SpaceExhausted(Exception):
    pass

class Space:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self._stack = []
        self._notes = []
        self._loc = -1
        self._exhausted = False

    def _rewind(self):
        self._loc = -1
        self._notes.clear()

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

    def note(self, note):
        self._notes.append(note)
        if self.verbose:
            print(f'Note: {note}')


class SpaceIterable:
    def __init__(self, fn, return_notes=False, verbose=False):
        self.fn = fn
        self.return_notes = return_notes
        self.verbose = verbose

    def __iter__(self):
        space = Space(verbose=self.verbose)
        try:
            while True:
                space._rewind()
                result = self.fn(space)
                if self.return_notes:
                    yield result, list(space._notes)
                else:
                    yield result
        except SpaceExhausted:
            pass


def iterate(fn, return_notes=False, verbose=False):
    return SpaceIterable(fn, 
        return_notes=return_notes,
        verbose=verbose)
