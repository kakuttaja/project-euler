

def create_sums(size, rolls, running_sum=0, counts=None):
    # Simulates the amount of possible dice roll sums
    if not counts:
        counts = {a: 0 for a in range(6, rolls*size + 1)}
    if rolls == 0:
        counts[running_sum] += 1
        return counts
    for i in range(1, size + 1):
        counts = create_sums(size, rolls-1, running_sum + i, counts)
    return counts

def main() -> None:
    ptr_sums = create_sums(size=4, rolls=9)
    col_sums = create_sums(size=6, rolls=6)
    # The number of possible rolls for both participants
    ptr_rolls = sum([int(i) for i in ptr_sums.values()]) # 4^9
    col_rolls = sum([int(i) for i in col_sums.values()]) # 6^6
    # Solve for the ratio of the amount of roll sums Peter wins over Colin
    win_percentage = 0
    for roll, count in ptr_sums.items():
        if count == 0:
            continue
        wins = 0
        # Count the games this roll beat
        for i in range(6, roll):
            wins += col_sums[i]
        # Calculate the portion of games won from Colin's total games
        colin_lost = wins / col_rolls
        # And use the percentage of Colin's games won to calculate
        # a running sum of games won proportionally to Peter's total games
        # (the weight of that roll's wins)
        win_percentage += colin_lost * (count / ptr_rolls)
    return round(win_percentage, 7)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")