

def load_pyramid() -> list:
    pyramid = []
    with open("067_triangle.txt", "r") as f:
        for line in f.readlines():
            pyramid.append([int(i) for i in line.split()])
    return pyramid

def main():
    # Algorithm starts from the top and replaces all the numbers
    # with the maximum value that number can lead to.
    # The highest value in the bottom row is the maximum total.
    pyramid = load_pyramid()
    for i in range(len(pyramid)):
        if i == 0:
            running_sum = pyramid[i][0]
            continue
        for j in range(len(pyramid[i])):
            top_sum = pyramid[i-1][max(0, j-1)]
            right_sum = pyramid[i-1][min(len(pyramid[i-1]) - 1, j)]
            running_sum = max(top_sum, right_sum)
            pyramid[i][j] = running_sum + pyramid[i][j]
    return max(pyramid[len(pyramid) - 1])


if __name__ == '__main__':
    print(main())
