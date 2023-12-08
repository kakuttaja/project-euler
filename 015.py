from time import perf_counter
from collections import defaultdict

def main() -> int:
    # Idea is to create a grid where
    # Both final straights have only one choice on where to move,
    # as there really is only one way to go: either right or down.
    # 
    # After that, every path next to the predetermined 1-way-paths
    # have two possible choices on where to go, and the total
    # choices will be the sum of the choices within the possible paths.
    # 
    # Total sum of all possible paths will be calculated to (0, 0).
    grid = []
    x, y = 21, 21
    for row in range(y - 1):
        grid.append([0] * (x - 1) + [1])
    grid.append([1] * x)
    for row in range(y - 1, -1, -1):
        for col in range(x - 1, -1, -1):
            if grid[row][col] == 0:
                next_row = grid[row + 1][col]
                next_col = grid[row][col + 1]
                grid[row][col] = next_row + next_col
    return grid[0][0]

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 4)}s")