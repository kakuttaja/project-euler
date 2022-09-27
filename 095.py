from typing import List

FALSE_NUMBERS = set()

def divisors(num) -> List[int]:
    return [int(i) for i in range(1, (num//2) + 1) if num % i == 0]

def amicable(num) -> int:
    val = num
    steps = set()
    while num < 10**6 and num > 1:
        # Check if number is already known to lead to a False
        if num in FALSE_NUMBERS:
            break
        steps.add(num)
        num = sum(divisors(num))
        # A perfect number
        if sum(divisors(num)) == num:
            break
        # A sociable number chain found
        if num == val and len(steps) > 1:
            return steps
        # Either an amicable pair, or an infinite loop
        if num in steps and len(steps) > 1:
            return False
    FALSE_NUMBERS.update(steps)
    return False

def main() -> None:
    best = 0
    result = None
    for i in range(1, 15000):
        res = amicable(i)
        if res and len(res) > best:
            print(i, "-->", min(res))
            result = min(res)
            best = len(res)
    return result

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")