

def load_grid():
    grid = []
    with open("081_matrix.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            grid.append([int(i) for i in line.split(",")])
    return grid

def main():
    # This function works in the same way as the one in 067.py
    # By replacing every single value from top-left to bottom-right
    # with the min() between the values to the left and the top,
    # we can create the minimum path in iterations.
    grid = load_grid()
    for i in range(len(grid)):
        for j in range(0, len(grid[i])):
            if i == 0 and j == 0:
                continue
            value = 0
            if i > 0:
                if j > 0:
                    value = min(grid[i - 1][j], grid[i][j - 1])
                else:
                    value = grid[i - 1][j]
            else:
                if j > 0:
                    value = grid[i][j - 1]
                else:
                    value = grid[i][j]
            grid[i][j] += value
    return grid[-1][-1]

if __name__ == '__main__':
    print(main())
