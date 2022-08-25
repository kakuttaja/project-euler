

def cancel_digits(x, y) -> bool:
    found = False
    result = x / y
    new_x = ""
    x = [str(i) for i in str(x)]
    y = [str(i) for i in str(y)]
    for i in range(len(x)):
        if x[i] in y:
            y.remove(x[i])
            found = True
            if x[i] == '0' and i == len(x) - 1:
                return False
            continue
        new_x += x[i]
    if not found or not new_x or not y: # Check if any modifications were made or if there are numbers remaining
        return False
    if int(new_x) == 0 or int(''.join(y)) == 0: # Check if either number is 0; don't want any division by zero shenanigans
        return False
    return result == int(new_x) / int(''.join(y))

def main() -> None:
    nums = 0
    ans = 1
    x = 1
    y = 2
    while nums < 4:
        x += 1
        if x == y:
            x = 1
            y += 1
            continue
        if cancel_digits(x, y):
            nums += 1
            ans *= x # Numerator
            ans /= y # Denominator
    return int(1 / ans)

if __name__ == '__main__':
    import time
    start = time.time()
    print(main())
    print(f"This took {round(time.time() - start, 2)}s")