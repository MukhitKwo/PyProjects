import json
import math
import re
from time import sleep
import copy

def sudoku():
    with open("sudoku/sudoku.json", "r") as file:
        data = json.load(file)

    grid_name = "grid1"

    grid = data[grid_name]
    possibility_grid = [row[:] for row in grid]

    for row in grid:
        print(row)

    while True:

        temp_grid = copy.deepcopy(possibility_grid)

        _get_possible_values(grid, possibility_grid)

        if possibility_grid == temp_grid:
            print("Stuck!")
            break

        zeros = _print_grid(possibility_grid)
        if zeros == 0:
            print("Solved!")
            break

        sleep(0.1)  # FOR TESTING


def _get_possible_values(grid, possibility_grid):

    numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for nRow, line in enumerate(grid):
        for nCol, num in enumerate(line):

            if num == 0:

                a = _get_lines_existing_values(grid, nRow, nCol)
                b = _get_square_existing_values(grid, nRow, nCol)

                possible = numbers.difference(a.union(b))

                if len(possible) == 1:
                    val = possible.pop()
                    grid[nRow][nCol] = val
                    possibility_grid[nRow][nCol] = val
                else:
                    possibility_grid[nRow][nCol] = possible


def _get_lines_existing_values(grid, row, col):
    exist = set()

    for px in range(0, 9):
        n = grid[row][px]
        if n == 0:
            continue

        exist.add(n)

    for py in range(0, 9):
        n = grid[py][col]
        if n == 0:
            continue
        exist.add(n)

    return exist


def _get_square_existing_values(grid,  row, col):

    x = math.floor(col/3)  # 0, 1 or 2
    y = math.floor(row/3)  # 0, 1 or 2

    r1 = grid[y * 3][(x * 3): (x*3 + 3)]
    r2 = grid[y * 3 + 1][(x * 3): (x*3 + 3)]
    r3 = grid[y * 3 + 2][(x * 3): (x*3 + 3)]

    exist = set(r1 + r2 + r3)
    exist.discard(0)
    return exist


def _print_grid(grid):

    zeros = 0

    print("===========================")

    for row in grid:
        print("[", end="")
        for col, num in enumerate(row):

            zeros += (1 if isinstance(num, set) else 0)

            if col < 8:

                if isinstance(num, set):
                    print(f"\033[91m{num}\033[0m", end=", ")
                else:
                    print(f"\033[92m{num}\033[0m", end=", ")
            else:
                if isinstance(num, set):
                    print(f"\033[91m{num}\033[0m", end="")
                else:
                    print(f"\033[92m{num}\033[0m", end="")
        print("]")
    return zeros


if __name__ == "__main__":
    sudoku()
