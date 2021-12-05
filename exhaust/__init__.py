"Exhaustively enumerate a combinatorial space represented by a function"

__version__ = "1.1.0"

from typing import (
    Callable, TypeVar, Iterable, Iterator,
    Sequence, Optional, List,
    overload
)
import itertools

class SpaceExhausted(Exception):
    pass

T = TypeVar('T')

class State:
    """
    An instance of this class is passed as argument to the
    function passed to :func:`~exhaust.space`.
    """
    def __init__(self, verbose: bool=False):
        self.verbose = verbose
        self._stack = []
        self._loc = -1
        self._exhausted = False

    def _rewind(self) -> None:
        self._loc = -1

    def choice(self, seq: Iterable[T]) -> T:
        """
        Return an element from the non-empty sequence ``seq``.

        This is the equivalent of :func:`random.choice`.

        :param seq: The sequence from which to choose from.
        :raises IndexError: if ``seq`` is empty.
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
                raise IndexError('empty sequence')
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

    def choices(self, population: Iterable[T], *, k: int=1) -> List[T]:
        """
        Return a ``k`` sized list of elements chosen from the ``population``
        with replacement.

        This is the equivalent of :func:`random.choices`, minus the
        ``weights`` and ``cum_weights`` arguments.

        :param population: The population from which to choose from.
        :param k: The number of elements to choose.
        :raise IndexError: if ``population`` is empty.
        """
        def _choices(population, k):
            for tup in itertools.combinations_with_replacement(population, k):
                yield list(tup)
        
        return self.choice(_choices(population, k))

    def sample(self, population: Sequence[T], k: int, *, counts: Optional[Iterable[int]]=None) -> List[T]:
        """
        Return a ``k`` sized list of unique elements chosen from
        the ``population``.

        This is the equivalent of :func:`random.sample`.

        :param population: The population from which to choose from.
        :param k: The number of elements to choose.
        :param counts: The number of times each element is repeated.
        :raise ValueError: if ``k`` is larger than the ``population`` size.
        """
        def _repeated(population, counts):
            for item, count in zip(population, counts):
                yield from itertools.repeat(item, count)

        def _sample(population, k):
            for tup in itertools.combinations(population, k):
                yield list(tup)
        
        n = len(population)
        if counts is not None:
            counts = list(counts)
            if len(counts) != n:
                raise ValueError('The number of counts does not match the population')
            total = sum(counts)
            if total <= 0:
                raise ValueError('Total of counts must be greater than zero')
            population_ = _repeated(population, counts)
        else:
            total = n
            population_ = population

        if k > total:
            raise ValueError('Sample larger than population or is negative')

        return self.choice(_sample(population_, k))

    def maybe(self) -> bool:
        """
        Return ``True`` or ``False``.
        Alias for ``choice([True, False])``.
        """
        return self.choice([True, False])

    @overload
    def randrange(self, stop: int) -> int:
        ...

    @overload
    def randrange(self, start: int, stop: int, step: Optional[int]=None) -> int:
        ...

    def randrange(self, *args) -> int:
        """
        Return an element from ``range(start, stop, step)``.

        This is the equivalent of :func:`random.randrange`.

        :param start: The start of the range.
        :param stop: The end of the range (exclusive).
        :param step: The step size.
        :raise ValueError: if the range is empty.
        """
        r = range(*args)
        if len(r) == 0:
            raise ValueError('empty range')
        return self.choice(r)

    def randint(self, a: int, b: int) -> int:
        """
        Return an integer ``N`` such that ``a <= N <= b``.
        Alias for ``randrange(a, b+1)``.

        This is the equivalent of :func:`random.randint`.

        :param a: The start of the range.
        :param b: The end of the range (inclusive).
        :raises ValueError: if the range is empty.
        """
        return self.randrange(a, b + 1)


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
    Return an iterable that generates values from ``fn``
    fully exhausting the state space.

    During iteration, the function ``fn`` is called repeatedly with a
    :class:`~exhaust.State` instance as only argument.

    :param fn: The function to generate values from.
    :param verbose: If True, print the state of the generator.
    """
    return SpaceIterable(fn, verbose=verbose)

__all__ = ['State', 'space']
