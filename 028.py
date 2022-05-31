

def get_other_corners(num, side):
    # Calculates the sum of the numbers 
    # in all the corners in current iteration of the spiral. 
    value = 0
    for i in range(1, 4):
        value += num + (i * side)
    return value + num


def main():
    ans = 1
    start = 3
    side = 2
    # 500 times for a 1001x1001 grid; 1 in the center makes it a 1000+1 x 1000+1.
    for _ in range(500):
        summed_corners = get_other_corners(start, side)
        ans += summed_corners
        # The new bottom-right corner has the value of
        # 3 * side-length + (new side-length) of the new loop
        start += (3 * side + side + 2)
        # The length of the side (space between corners)
        # always increases by 2 every loop of the spiral
        side += 2
    return ans

if __name__ == '__main__':
    print(main())
