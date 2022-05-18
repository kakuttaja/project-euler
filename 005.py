

def main():
    # Brute-force method
    limit = 20
    a = 20
    while True:
        for i in range(limit, 0, -1):
            if not a % i == 0:
                break
            if i == 1:
                return a
        a += 20

if __name__ == '__main__':
    print(main())