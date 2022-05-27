

def get_divisors_sum(n) -> int:
    ans = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans += i
    return ans

def main():
    ans = 0
    ignore_list = []
    for i in range(1, 10000):
        if i in ignore_list:
            continue
        divs = get_divisors_sum(i)
        if divs != i:
            if get_divisors_sum(divs) == i:
                ans += i + divs
                ignore_list.append(divs)
    return ans


if __name__ == '__main__':
    print(main())
