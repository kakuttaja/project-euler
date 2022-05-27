import math

def factorial(n) -> int:
    return math.prod([int(i) for i in range(1, n + 1)])

def main():
    return sum([int(i) for i in str(factorial(100))])


if __name__ == '__main__':
    print(main())
