from time import perf_counter
from math import inf, sqrt, pow
import functools

@functools.cache
def gen_point(n: int) -> int:
    if n <= 0:
        return 290797
    return (gen_point(n - 1) ** 2 ) % 50515093

def dist(a: tuple, b: tuple) -> int:
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def get_best(points: list) -> int:
    m = inf
    for p1 in points:
        for p2 in points:
            if p1 == p2: continue
            D = round(dist(p1, p2), 9)
            if D < m:
                m = D
    return m

def divcon(points: list) -> int:
    # Divide-and-conquer algorithm to split the search space into two recursively
    # in the x-axis, and create a bound from the recursive paths by getting
    # a minimum distance within those two splits.
    # 
    # For example, if the min distance is found between points both in the left group,
    # no higher nodes will be searched, because the answer won't change.
    # 
    # Pretty much the same as a binary search, I suppose.
    # https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
    # https://www.cs.ubc.ca/~liorma/cpsc320/files/closest-points.pdf

    # Bruteforce min if three points remain, otherwise no need.
    if len(points) <= 3:
        if len(points) == 1: 
            return inf
        elif len(points) == 2: 
            return dist(points[0], points[1])
        return get_best(points)
    mid = len(points) // 2

    # Get median x-value from points
    if len(points) % 2 == 0:
        xmid = (points[mid - 1][0] + points[mid][0])/2
    else:
        xmid = points[mid][0]
    
    L, R = points[:mid], points[mid:]
    dl = divcon(L)
    dr = divcon(R)
    # Minimum distances found between points in both groups.
    d = min(dl, dr)
    # Disregard nodes that won't fit the search conducted between L and R.
    L = [l for l in L if xmid - d < l[0] < xmid + d]
    R = [r for r in R if xmid - d < r[0] < xmid + d]
    # Compare nodes in L and R, disregard nodes in R that won't fit L.
    for p1 in L:
        for p2 in [p for p in R if p1[0] < p[0] < p1[0] + d and p1[1] - d < p[1] < p1[1] + d]:
            newdist = round(dist(p1, p2), 9)
            if newdist < d:
                d = newdist
    return d

def main() -> None:
    points = []
    best = inf
    lim = 2000000
    for n in range(lim):
        p = (gen_point(2 * n), gen_point((2 * n) + 1))
        points.append(p)
    best = divcon(sorted(points))
    return best

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")