
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    products = {}
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            fx = n ** 2 + a * n + b
            while is_prime(fx):
                n += 1
                fx = n ** 2 + a * n + b
            if n > products.get(a * b, 0):
                products[a * b] = n
    return max(products.keys(), key=lambda x: products[x])

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")