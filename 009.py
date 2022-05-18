

def main():
    ans = 0
    for a in range(1, 1000):
        for b in range(a + 1, 1000-a):
            c = (a**2 + b**2)**0.5
            if c % 1 != 0:
                continue
            if a + b + c > 1000:
                break
            if a + b + c == 1000:
                return int(a*b*c)
    return ans

if __name__ == '__main__':
    print(main())