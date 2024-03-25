from itertools import count

def main() -> int:
    # x > y > z > 0
    # let x + y = a ** 2
    # and x - y = b ** 2
    # 
    # => x = (a ** 2 + b ** 2) / 2
    # y = a ** 2 - x
    # z = c ** 2 - x
    # a > c > b
    # 
    # because z = c ** 2 - x > 0
    # therefore c > sqrt(x)
    squares = {i ** 2: True for i in range(1, int(1000000 ** 0.5) + 1)}
    for a in count(3):
        # a ** 2 + b ** 2 must be divisible by 2
        # as x = (a ** 2 + b ** 2) / 2 
        # and x is an integer
        # therefore if a is even, b must be even as well,
        # and if a is odd, b must also be odd.
        s = 1
        if a % 2 == 0:
            s = 2
        for b in range(s, a, 2):
            x = (a ** 2 + b ** 2) / 2
            y = a ** 2 - x
            if x <= y or b >= int(x ** 0.5):
                break
            for c in count(int(x ** 0.5)):
                z = c ** 2 - x
                if y <= z:
                    break
                if all(
                    squares.get(i, False) for i in [
                        x - z, y + z, y - z
                    ]):
                    return int(x + y + z)
    return 0

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")