import pytest
import exhaust

def test_combined():
    def gen(state: exhaust.State):
        return (state.maybe(),
                state.randint(1, 3),
                state.choice(['a', 'b', 'c', 'd', 'e']))

    assert len(set(exhaust.space(gen))) == 2 * 3 * 5

def test_choice():
    def gen(state: exhaust.State):
        return state.choice(['a', 'b', 'c'])

    assert set(exhaust.space(gen)) == set(['a', 'b', 'c'])

def test_choice_with_empty_sequence_raises():
    def gen(state: exhaust.State):
        state.choice([])

    with pytest.raises(IndexError):
        for _ in exhaust.space(gen):
            pass

def test_choices():
    def gen(state: exhaust.State):
        return state.choices(['a', 'b', 'c'], k=2)
    
    assert list(exhaust.space(gen)) == [
        ['a', 'a'],
        ['a', 'b'],
        ['a', 'c'],
        ['b', 'b'],
        ['b', 'c'],
        ['c', 'c'],
    ]

def test_choices_with_empty_sequence_raises():
    def gen(state: exhaust.State):
        state.choices([])

    with pytest.raises(IndexError):
        for _ in exhaust.space(gen):
            pass

def test_sample():
    def gen(state: exhaust.State):
        return state.sample([1, 2, 3], k=2)
    
    assert list(exhaust.space(gen)) == [
        [1, 2], [1, 3], [2, 3]
    ]

def test_sample_with_counts():
    def gen(state: exhaust.State):
        return state.sample([1, 2], k=2, counts=[1, 2])
    
    assert list(exhaust.space(gen)) == [
        [1, 2], [1, 2], [2, 2]
    ]

def test_sample_with_counts_mismatching_population():
    def gen(state: exhaust.State):
        return state.sample([1, 2], k=2, counts=[1, 2, 2])
    
    with pytest.raises(ValueError):
        for _ in exhaust.space(gen):
            pass

def test_sample_with_counts_totalling_zero():
    def gen(state: exhaust.State):
        return state.sample([1, 2], k=2, counts=[0, 0])
    
    with pytest.raises(ValueError):
        for _ in exhaust.space(gen):
            pass

def test_sample_with_k_larger_than_population_raises():
    def gen(state: exhaust.State):
        state.sample([1, 2, 3], k=4)

    with pytest.raises(ValueError):
        for _ in exhaust.space(gen):
            pass

def test_sample_with_k_larger_than_population_with_counts_raises():
    def gen(state: exhaust.State):
        state.sample([1, 2, 3], k=5, counts=[1, 2, 1])

    with pytest.raises(ValueError):
        for _ in exhaust.space(gen):
            pass

def test_maybe():
    def gen(state: exhaust.State):
        return state.maybe()

    assert set(exhaust.space(gen)) == set([False, True])

def test_randrange_start_stop_step():
    def gen(state: exhaust.State):
        return state.randrange(0, 10, 2)

    assert set(exhaust.space(gen)) == set([0, 2, 4, 6, 8])

def test_randrange_start_stop():
    def gen(state: exhaust.State):
        return state.randrange(1, 3)

    assert set(exhaust.space(gen)) == set([1, 2])

def test_randrange_stop():
    def gen(state: exhaust.State):
        return state.randrange(3)

    assert set(exhaust.space(gen)) == set([0, 1, 2])

def test_randint():
    def gen(state: exhaust.State):
        return state.randint(1, 3)

    assert set(exhaust.space(gen)) == set([1, 2, 3])
