Pool Rack Solver

A small Python project that finds the minimum number of ball swaps required to transform a randomly arranged English pool rack into the standard International Rules yellow-tick rack.

Rack Representation

The rack contains:

* 7 red balls (R)
* 7 yellow balls (Y)
* 1 black ball (B)

Positions are numbered from 1 to 15, starting at the apex and moving left-to-right through each row.

The target rack is:

        R 
      Y   R
    R   B   Y
  Y   R   Y   R
R   Y   Y   R   Y

How It Works

The solver compares the current rack with the target rack and identifies incorrectly positioned balls.

It first finds pairs of positions where swapping the two balls corrects both positions. After these swaps, any remaining incorrect positions form a three-ball cycle, which can be solved in two swaps.

The returned swap positions use 1-based numbering to correspond to physical positions in the rack.

Example

from pool_rack_solver.rack import solve_rack
rack = ['R','R','Y','B','Y','R','Y','R','Y','Y','R','Y','Y','R','R']
print(solve_rack(rack))

Example output:

Swaps required: [(2, 3), (10, 15), (4, 5), (4, 6)]

Testing

Tests are written using pytest and can be run with:

pytest