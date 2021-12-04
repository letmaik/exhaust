import exhaust

def test_double_iteration():
    def gen(state: exhaust.State):
        return state.maybe()

    space = exhaust.space(gen)
    assert len(set(space)) == 2
    assert len(set(space)) == 2
