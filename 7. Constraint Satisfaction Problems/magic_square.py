from typing import NamedTuple, cast
from csp import Constraint, CSP
from itertools import permutations, batched


type Grid = list[list[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def check_square(square: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = square
    return    ((a + b + c) # Rows
            == (d + e + f)
            == (g + h + i)
            == (a + d + g) # Columns
            == (b + e + h)
            == (c + f + i)
            == (a + e + i) # Diagonals
            == (g + e + c))


def convert_to_grid(assignment: dict[int, GridLocation]) -> Grid:
    square: Grid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for var, (row, col) in assignment.items():
        square[row][col] = var
    return square


class MagicSquareConstraint(Constraint[int, GridLocation]):

    def __init__(self, variables: list[int]):
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[int, GridLocation]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False
        if len(assignment) < 9:
            return True
        return check_square(convert_to_grid(assignment))


def solve_csp():
    variables: list[int] = list(range(1, 10))
    all_grid_locations: list[GridLocation] = [GridLocation(r, c) for r in range(3)
                                                                 for c in range(3)]
    domains: dict[int, list[GridLocation]] = {
        var: all_grid_locations for var in variables
    }
    csp: CSP[int, GridLocation] = CSP(variables, domains)
    csp.add_constraint(MagicSquareConstraint(variables))
    solution: dict[int, GridLocation] | None = csp.backtracking_search()
    if solution:
        print(convert_to_grid(solution))
    else:
        print('Found no solution :(')


def solve_brute_force():
    for p in permutations(range(1, 10)):
        grid: list[tuple[int, ...]] = list(batched(p, 3))
        if check_square(cast(Grid, grid)):
            print(grid)


if __name__ == '__main__':
    solve_csp()
    solve_brute_force()
