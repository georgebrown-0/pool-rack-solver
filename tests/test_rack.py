from pool_rack_solver.rack import validate_rack, get_incorrect_positions, get_opposite_pairs

def test_validate_rack():
    rack = ['R','Y','R','R','B','Y','Y','R','Y','R','R','Y','Y','R','Y']
    validate_rack(rack)

def test_get_incorrect_positions():
    rack = ['Y','R','R','R','B','Y','Y','R','Y','R','R','Y','Y','R','Y']
    incorrect_positions = get_incorrect_positions(rack)
    expected_incorrect_positions = {0: ('Y', 'R'), 1: ('R', 'Y')}
    assert incorrect_positions == expected_incorrect_positions

def test_get_opposite_pairs():
    rack = ['Y','R','R','B','R','Y','Y','Y','R','R','R','Y','Y','R','Y']
    opposite_pairs = get_opposite_pairs(get_incorrect_positions(rack))
    expected_opposite_pairs = [(0, 1), (3, 4), (7, 8)]
    assert opposite_pairs == expected_opposite_pairs