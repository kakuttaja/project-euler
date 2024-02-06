
def triangle(n):
    return n * (n + 1) / 2
def square(n):
    return n ** 2
def penta(n):
    return n * (3 * n - 1) / 2
def hexa(n):
    return n * (2 * n - 1)
def hepta(n):
    return n * (5 * n - 3) / 2
def octa(n):
    return n * (3 * n - 2)

def rec(n, functions, r, path, nums):
    if all(f in path.keys() for f in functions) and n // 100 == nums[0] % 100:
        return sum(nums)
    for f in functions:
        if f in path.keys():
            continue
        for n2 in r[f]:
            if n2 % 100 == n // 100:
                path[f] = n2
                ans = rec(n2, functions, r, path, nums + [n2])
                path.pop(f)
                if ans is not None:
                    return ans
    return None

def main():
    # Quite simple to do by gathering all the
    # numbers from each function [1000, 9999]
    # and then recursively going through all
    # functions and their respective numbers
    # to find a sequence of numbers that is ordered
    # with the rule n // 100 == n2 % 100.
    r = {}
    n = 1
    functions = (triangle, square, penta, hexa, hepta, octa)
    while triangle(n) < 10000:
        for func in functions:
            a = func(n)
            if 1000 < a < 10000:
                if r.get(func, None) is None:
                    r[func] = []
                r[func].append(int(a))
        n += 1
    ans = None
    for n in r[triangle]:
        res = rec(n, functions, r, {triangle: n}, [n])
        if res:
            ans = res
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")