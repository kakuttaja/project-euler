

def load_pyramid() -> list:
    pyramid = []
    with open("018_pyramid.txt", "r") as f:
        for line in f.readlines():
            pyramid.append([int(i) for i in line.split()])
    return pyramid

def pyramid_solver(pyramid, i, j) -> int:
    # Wouldn't want to have indices below 0 or higher than len(pyramid[i])
    if j < 0 or j >= len(pyramid[i]):
        return 0
    # Reached the top of the pyramid: return the top value
    if i == 0:
        return pyramid[i][j]
    # Return the sum of current node and max(future possibilities) 
    # to get the total max value this node can result in
    return pyramid[i][j] + max(pyramid_solver(pyramid, i - 1, j - 1), pyramid_solver(pyramid, i - 1, j))


def main():
    pyramid = load_pyramid()
    ans = []
    # For each starting point, could start from the top to get rid of this for-loop...
    for i in range(len(pyramid[len(pyramid) - 1])):
        ans.append(pyramid_solver(pyramid, len(pyramid) - 1, i))
    return max(ans)


if __name__ == '__main__':
    print(main())
