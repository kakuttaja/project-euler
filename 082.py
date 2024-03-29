from time import perf_counter
from queue import PriorityQueue
from math import inf

def get_map() -> tuple:
    map = []
    with open(f"082.txt", "r") as f:
        for l in f.readlines():
            map.append(tuple([int(i) for i in l.strip().split(",")]))
    return tuple(map)

def is_valid(pos: tuple, map: tuple) -> bool:
    return 0 <= pos[0] < len(map[0]) and 0 <= pos[1] < len(map)

def add_pos(pos: tuple, dir: tuple) -> tuple:
    return pos[0] + dir[0], pos[1] + dir[1]

def generate_move(state: tuple, map: tuple) -> tuple:
    pos, dist, dir = state
    moves = []
    for m in [(1, 0), (0, 1), (0, -1)]:
        new_pos = add_pos(pos, m)
        x, y = new_pos
        if is_valid(new_pos, map):
            new_dist = dist + map[y][x]
            moves.append(tuple([new_dist, (new_pos, new_dist, m)]))
    return moves

def main() -> None:
    map = get_map()
    end = len(map[0]) - 1
    moves = {}
    best = inf
    for _y in range(len(map)):
        queue = PriorityQueue()
        x, y = (0, _y)
        state = (x, _y), map[_y][x], None
        queue.put((map[_y][x], state))
        while not queue.empty():
            if queue.empty():
                break
            dist, state = queue.get(False)
            (x, y), dist, dir = state
            moves[(x, y, dir)] = dist
            if x == end:
                if dist < best:
                    best = dist
                continue
            if dist >= best:
                continue
            for (cost, move) in generate_move(state, map):
                (x2, y2), dist, dir = move
                if cost < moves.get((x2, y2, dir), inf) and cost < best:
                    queue.put((cost, move))
    return best

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")