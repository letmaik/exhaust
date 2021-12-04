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

def test_maybe():
    def gen(state: exhaust.State):
        return state.maybe()

    assert set(exhaust.space(gen)) == set([False, True])

def test_randint():
    def gen(state: exhaust.State):
        return state.randint(1, 3)

    assert set(exhaust.space(gen)) == set([1, 2, 3])

