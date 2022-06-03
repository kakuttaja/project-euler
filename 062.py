

def get_original_cubes(number, length):
    # Returns the first cube that fits the permutation
    x = 1
    while True:
        cube = x**3
        temp = [str(i) for i in str(cube)]
        temp.sort()
        if ''.join(temp) == number:
            return cube
        x += 1

def main():
    # Use a hashed list (dictionary) to save the amount of
    # number sequences that have certain numbers (ordered list-representations of cubes)
    # searches for the lowest cube after finding 5 matches for a set of numbers
    ans = 0
    permutation = {}
    x = 1
    limit = 5
    while True:
        cube = x**3
        temp = [str(i) for i in str(cube)]
        temp.sort()
        temp = ''.join(temp)
        if temp in permutation.keys():
            permutation[temp] += 1
        else:
            permutation[temp] = 1
        if limit in permutation.values():
            for k, v in permutation.items():
                if v == limit:
                    ans = k, v
                    break
            break
        x += 1
    return get_original_cubes(*ans)

if __name__ == '__main__':
    print(main())
