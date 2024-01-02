from time import perf_counter


def in_triangle(p: tuple, v: tuple) -> bool:
    # A true programmer doesn't think, and just relies on StackOverflow.......?
    p0, p1, p2 = v
    A = 1/2 * (-p1[1] * p2[0] + p0[1] * (-p1[0] + p2[0]) + p0[0] * (p1[1] - p2[1]) + p1[0] * p2[1])
    sign = -1 if A < 0 else 1
    s = (p0[1] * p2[0] - p0[0] * p2[1] + (p2[1] - p0[1]) * p[0] + (p0[0] - p2[0]) * p[1]) * sign
    t = (p0[0] * p1[1] - p0[1] * p1[0] + (p0[1] - p1[1]) * p[0] + (p1[0] - p0[0]) * p[1]) * sign
    return s > 0 and t > 0 and (s + t) < 2 * A * sign

def main() -> None:
    triangles = list()
    with open("102.txt") as f:
        for line in f.readlines():
            points = []
            line = line.strip().split(",")
            for i in range(0, len(line) - 1, 2):
                points.append((int(line[i]), int(line[i + 1])))
            triangles.append(points)
    return sum([in_triangle((0, 0), v) for v in triangles])

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")