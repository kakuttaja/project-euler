

def main() -> str:
    return str(sum([int(i ** i) for i in range(1, 1001)]))[-10:]

if __name__ == "__main__":
    print(main())