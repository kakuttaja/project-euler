from itertools import permutations

def main():
    # Itertools.permutations generates permutations lexicographically!
    ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    best = 0
    best_order = 0
    for perm in permutations(ans):
        num = int(''.join(str(i) for i in perm))
        if num > best:
            best_order += 1
            if best_order == 10**6:
                return num
            best = num
    return 0

if __name__ == '__main__':
    print(main())
