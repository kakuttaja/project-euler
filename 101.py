from time import perf_counter
from math import prod
import sympy

def main() -> int:
    # Lagrange polynomials!
    # https://en.wikipedia.org/wiki/Lagrange_polynomial
    # 
    # As P(1) will always be incorrect by 1,
    # it will be directly added to the answer.
    # 
    # Sympy is very nice!
    # Never had a case to use it before.
    # Though it isn't absolutely needed,
    # as substitution can be done iteratively instead
    # ..me thinks. Probably.
    ans = 0
    y = [sum((-n) ** k for k in range(11)) for n in range(1, 13)]
    x = sympy.symbols('x')
    for i in range(2, len(y)):
        nums = list(range(1, i + 1))
        v = 0
        for k in range(len(nums)):
            p = prod([(x - nums[j]) / (nums[k] - nums[j]) for j in range(len(nums)) if j != k])
            v += p * y[k]
        if not isinstance(v, int):
            for m in range(len(y)):
                v2 = v.subs(x, m + 1)
                if v2 != y[m]:
                    ans += v2
                    break
    return ans + 1

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")