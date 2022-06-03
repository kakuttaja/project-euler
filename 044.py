

def main():
    # Minimized D = |Pk - Pj| is the first pentagonal pair found,
    # due to the fact that the difference increases with every nth pentagonal number (I think..)
    # Less readability due to performance gain with fewer function calls
    # for both is_penta() checking as well as penta number generation
    a = 1
    while True:
        p1 = int((a * (3 * a - 1))/2)
        for i in range(1, a):
            p2 = int((i * (3 * i - 1))/2)
            if (((24*(p1-p2) + 1)**0.5 + 1) / 6) % 1 == 0 and (((24*(p2+p1) + 1)**0.5 + 1) / 6) % 1 == 0:
                return (p1-p2)
        a += 1

if __name__ == '__main__':
    print(main())
