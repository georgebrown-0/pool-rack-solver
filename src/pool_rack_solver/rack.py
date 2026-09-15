target_rack = ['R','Y','R','R','B','Y','Y','R','Y','R','R','Y','Y','R','Y']

def validate_rack(rack: list) -> None:
    '''
    Validate that a rack has the correct length, ball counts, and entry types.

    Parameters
    ----------
    rack : list
        A list containing strings representing the balls in therack.
        rack must contain 15 string entries.
        entries must be one of 'R', 'Y', or 'B'.
        rack must contain 7 'R's, 7 'Y's, and 1 'B'.


    Raises
    ------
    TypeError
        If any entry in the rack is not a string.
    ValueError
        If the rack has an incorrect length, contains an invalid string, or 
        does not contain the required number of each ball type.
    '''
    if not isinstance(rack, list):
        raise TypeError('The rack must be a list')
    if len(rack) != 15:
        raise ValueError('The rack must have 15 entries')
    for r in rack:
        if not isinstance(r, str):
            raise TypeError('All entries in the rack must be strings')
        if r not in ['R', 'Y', 'B']:
            raise ValueError('All entries in the rack must be R, Y, or B')
    if rack.count('R') != 7 or rack.count('Y') != 7 or rack.count('B') != 1:
        raise ValueError('The rack must contain 7 Rs, 7 Ys, and 1 B')
    return None

def get_incorrect_positions(rack: list) -> dict:
    '''
    Get a dictionary of incorrect balls in the rack.

    Parameters
    ----------
    rack : list
        A list containing strings representing the balls in the rack.
        Assume rack has already been validated.

    Returns
    -------
    dict
        A dictionary containing the incorrect balls in the rack.
        Keys are the incorrect positions indices, and values are tuples of the form (current, target).
    '''
    incorrect_positions = {}
    for pos in range(len(rack)):
        if rack[pos] != target_rack[pos]:
            incorrect_positions[pos]=(rack[pos], target_rack[pos])
    return incorrect_positions

def get_opposite_pairs(incorrect_positions: dict) -> list:
    '''
    Find pairs of incorrect positions whose current and target balls are opposite.

    Parameters
    ----------
    incorrect_positions : dict
        A dictionary of incorrect rack positions.
        Keys are position indices, and values are tuples of the form
        (current, target).

    Returns
    -------
    list
        A list of tuples containing pairs of position indices whose balls
        can be swapped to correct both positions.
        Each pair is included only once.
    '''
    opposite_pairs = []
    reversed_pairs = {}
    already_seen = set()
    for pos, pair in incorrect_positions.items():
        reversed_pairs[pos]=((pair[::-1]))
    for pos, pair in incorrect_positions.items():
        for reversed_pos, reversed_pair in reversed_pairs.items():
            if pair == reversed_pair and pos < reversed_pos and pos not in already_seen and reversed_pos not in already_seen:
                opposite_pairs.append((pos, reversed_pos))
                already_seen.update((pos, reversed_pos))
    return opposite_pairs

def swap_balls(rack: list, pair: tuple) -> None:
    '''
    Swap the balls at the specified positions in the rack.

    Parameters
    ----------
    rack : list
        A list containing strings representing the balls in the rack.
        Assume rack has already been validated.
    pair : tuple
        A tuple containing the position indices of the balls to swap.
    
    Returns
    _______
    None
    '''
    rack[pair[0]], rack[pair[1]] = rack[pair[1]], rack[pair[0]]
    return None

def solve_rack(rack: list) -> str:
    '''
    Solve the rack using the minimum number of ball swaps.

    Parameters
    ----------
    rack : list
        A list containing strings representing the balls in the rack.
        The rack is validated before solving and is mutated as swaps are made.

    Returns
    -------
    str
        A message stating that no swaps are required if the rack is already
        correct, or the sequence of required swaps using positions 1 to 15.

    Raises
    ------
    TypeError
        If the rack or its entries have invalid types.
    ValueError
        If the rack has an invalid length, entries, or ball counts.
    '''
    validate_rack(rack)
    swaps = []
    if rack == target_rack:
        return "No swaps required"
    incorrect_positions = get_incorrect_positions(rack)
    opposite_pairs = get_opposite_pairs(incorrect_positions)
    for pair in opposite_pairs:
        swaps.append(tuple(p+1 for p in pair))
        swap_balls(rack, pair)
    if rack == target_rack:
        return f'Swaps required: {swaps}'
    incorrect_positions = get_incorrect_positions(rack)
    last = next(iter(incorrect_positions))
    positions = list(incorrect_positions.keys())
    positions.remove(last)
    swap_balls(rack, tuple(positions))
    swaps.append(tuple(p+1 for p in positions))
    incorrect_positions = get_incorrect_positions(rack)
    opposite_pairs = get_opposite_pairs(incorrect_positions)
    swap_balls(rack, opposite_pairs[0])
    swaps.append(tuple(p+1 for p in opposite_pairs[0]))
    return f'Swaps required: {swaps}'


    






