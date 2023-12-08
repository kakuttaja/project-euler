

def main() -> None:
    # Jumps to first day of every month and checks
    # if the day happens to be a Sunday (num_day % 7 == 0: Sunday)
    # The year 1901 started on a Tuesday, therefore the first day is base = 2.
    ans = 0
    months = {i: 31 if i not in (3, 5, 8, 10) else 30 for i in range(12)}
    months[1] = 28 # Unless its a leap year..
    current_month = 0
    current_year = 1901
    base = 2 # 1: Monday, 2: Tuesday, 3: Wednesday.. 7: Sunday
    while current_year < 2001:
        if current_month == 1 and (current_year % 4 == 0 or current_year % 400 == 0):
            base += 29
        else:
            base += months[current_month]
        current_month = (current_month + 1) % 12
        if current_month == 0:
            current_year += 1
        if base % 7 == 0: # The day is a Sunday
            ans += 1
    return ans

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}ms")