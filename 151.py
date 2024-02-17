import functools

def main():
    # Recursion to check every pattern
    # and how likely it is to reach a len == 1
    # state from that specific pattern to get a summed probability.
    # 
    # Monte Carlo simulation would be possible
    # but 6-digit accuracy requires way too many rounds.
    @functools.cache
    def rec(state: tuple) -> int:
        if not sum(state):
            return 0
        ans = 0
        if sum(state) == 1 and not state[0] + state[-1]:
            ans += 1
        for i in range(len(state)):
            if not state[i]:
                continue
            new_state = [i for i in state]
            new_state[i] -= 1
            for j in range(i + 1, len(state)):
                new_state[j] += 1
            # Probability of picking n-sized sheet out of all m sheets
            # is (x * n) / m, where x is the number n-sized sheets
            # and m is the total number of sheets to choose from.
            # 
            # P increases in relation to the number sheets of size state[i]
            # therefore P = sum(resulting len == 1 results) * (state[i] / sum(state))
            # where sum(state) == total number of choices
            ans += rec(tuple(new_state)) * (state[i] / sum(state))
        return ans
    return round(rec((1, 0, 0, 0, 0)), 6)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")