from time import perf_counter
from heapq import heappush, heappop

def main() -> int:
    # Fun problem for which the Prim's algorithm is just made for!
    # https://en.wikipedia.org/wiki/Prim%27s_algorithm
    # Aim is to just find the minimum spanning tree starting
    # from an arbitrary point. In my case, its the node 0.
    matrix = []
    with open("107.txt") as f:
        for l in f.readlines():
            matrix.append([int(i) if i.isnumeric() else "-" for i in l.strip().split(",")])
    chars = [i for i in range(len(matrix))]
    nodes = {}
    wt = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if isinstance(matrix[y][x], int):
                d = matrix[y][x]
                p1 = nodes.get(chars[x], None)
                p2 = nodes.get(chars[y], None)
                if not p1:
                    p1 = []
                if not p2:
                    p2 = []
                if (chars[y], d) not in p1 and (chars[x], d) not in p2:
                    p1.append((chars[y], d))
                    p2.append((chars[x], d))
                    wt += d
                nodes[chars[x]] = p1
                nodes[chars[y]] = p2
    q = []
    heappush(q, (0, 0))
    visited = []
    ans = 0
    while q:
        cost, node = heappop(q)
        if node in visited:
            continue
        ans += cost
        visited.append(node)
        for (child, dist) in nodes[node]:
            if child not in visited:
                heappush(q, (dist, child))
    return wt - ans

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")