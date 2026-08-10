import numpy as np

def E():

    def rad(n):
        # Can use the sieve for this efficiently?
        # Correct.
        # 
        # Shrimply can multiply each key by every
        # prime factor that arrives at the index.
        p = [True] * (n + 1)
        p[0], p[1] = False, False

        p_v = {k: 1 for k, _ in enumerate(range(n + 1))}

        for i in range(2, len(p)):
            if p[i]:
                p_v[i] = i
                for j in range(i * 2, len(p), i):
                    p[j] = False
                    p_v[j] *= i
        return list(dict(sorted(p_v.items(), key=lambda d: d[1])).keys())

    return np.array(rad(100_000))

def main():
    return E()[10_000]
    

if __name__ == '__main__':
    from time import perf_counter_ns
    start = perf_counter_ns()
    print(main())
    print(f"This took {round((perf_counter_ns() - start) / 1e6, 1)}ms")