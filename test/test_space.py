import exhaustive

def test_combined():
    def gen(space: exhaustive.Space):
        return (space.maybe(),
                space.randint(1, 3),
                space.choice(['a', 'b', 'c', 'd', 'e']))

    assert len(set(exhaustive.iterate(gen))) == 2 * 3 * 5

def test_choice():
    def gen(space: exhaustive.Space):
        return space.choice(['a', 'b', 'c'])

    assert set(exhaustive.iterate(gen)) == set(['a', 'b', 'c'])

def test_maybe():
    def gen(space: exhaustive.Space):
        return space.maybe()

    assert set(exhaustive.iterate(gen)) == set([False, True])

def test_randint():
    def gen(space: exhaustive.Space):
        return space.randint(1, 3)

    assert set(exhaustive.iterate(gen)) == set([1, 2, 3])

