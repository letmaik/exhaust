"The exhaust package"

__version__ = "1.0.0"

from typing import Callable, TypeVar, Iterable, Iterator, Optional, overload


class SpaceExhausted(Exception):
    pass

T = TypeVar('T')

class State:
    def __init__(self, verbose: bool=False):
        self.verbose = verbose
        self._stack = []
        self._loc = -1
        self._exhausted = False

    def _rewind(self) -> None:
        self._loc = -1

    def choice(self, seq: Iterable[T]) -> T:
        """
        Return an element from the non-empty sequence seq.
        If seq is empty, raises IndexError.
        """
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
                raise IndexError('Empty sequence')
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

    def maybe(self) -> bool:
        """
        Return either True or False.
        """
        return self.choice([True, False])

    @overload
    def randrange(self, stop: int) -> int:
        """
        Return an element from range(stop).
        """
        ...

    @overload
    def randrange(self, start: int, stop: int, step: Optional[int]=None) -> int:
        """
        Return an element from range(start, stop, step).
        """
        ...

    def randrange(self, *args) -> int:
        return self.choice(range(*args))

    def randint(self, a: int, b: int) -> int:
        """
        Return an integer N such that a <= N <= b.
        Alias for randrange(a, b+1).
        """
        return self.choice(range(a, b + 1))


class SpaceIterable(Iterable[T]):
    def __init__(self, fn: Callable[[State], T], verbose: bool=False):
        self.fn = fn
        self.verbose = verbose

    def __iter__(self) -> Iterator[T]:
        state = State(verbose=self.verbose)
        try:
            while True:
                state._rewind()
                yield self.fn(state)
        except SpaceExhausted:
            pass


def space(fn: Callable[[State], T], verbose: bool=False) -> Iterable[T]:
    """
    Return an iterable that generates values from fn.
    """
    return SpaceIterable(fn, verbose=verbose)

__all__ = ['State', 'space']
