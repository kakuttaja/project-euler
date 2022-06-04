from eulerlib import is_prime


def main():
    # Using diagonal number generation from 042.py
    start = 3
    side = 2
    target = 0.10
    diagonal_numbers = 1
    diagonal_primes = 0
    loops = 1
    while True:
        diagonal_numbers += 4
        for i in range(0, 4):
            if is_prime(start + (i * side)):
                diagonal_primes += 1
        if diagonal_primes/diagonal_numbers < target:
            return side + 1
        start += (3 * side + side + 2)
        side += 2
        loops += 1

if __name__ == '__main__':
    print(main())
