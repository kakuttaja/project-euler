
def load_puzzles() -> list[int]:
    games = []
    with open("096_sudoku.txt", "r") as f:
        temp = []
        for line in f.readlines():
            if "Grid" in line:
                if temp: games.append(temp)
                temp = []
                continue
            temp.append([int(i) for i in line.strip()])
        games.append(temp)
    return games

class Solver:
    def main(self) -> int:
        # Inefficient recursive brute-force algorithm
        # ~ 0.5s runtime using PyPy, ~ 20s Python
        puzzles = load_puzzles()
        self.current = None
        self.solution = 0
        self.options = {}

        for puzzle in puzzles:
            self.current = puzzle
            # Create possible nums for each tile
            for y, row in enumerate(self.current):
                for x, _ in enumerate(row):
                    raw_idx = y * 9 + x
                    self.options[raw_idx] = self.possible_nums(x, y)
                    if len(self.options[raw_idx]) == 1:
                        self.current[y][x] = next(iter(self.options[raw_idx]))
                        self.certain_numbers += 1
            self.solve()
        return self.solution

    def solve(self) -> int:
        flag = False
        for row in self.current:
            for n in row:
                if n == 0:
                    flag = True
                    break
            if flag: break
        if not flag:
            self.solution += 100 * self.current[0][0] + 10 * self.current[0][1] + self.current[0][2]
            return True
        for y in range(9):
            for x in range(9):
                if self.current[y][x] > 0: continue
                for num in self.options[y * 9 + x]:
                    if self.check_if_possible(x, y, num):
                        self.current[y][x] = num
                        if self.solve():
                            return True
                        self.current[y][x] = 0
                return False
        return False

    def possible_nums(self, x: int, y: int) -> set[int]:
        if self.current[y][x] > 0: return set([self.current[y][x]])
        nums = set()
        for n in range(1, 10):
            if self.check_if_possible(x, y, n):
                nums.add(n)
        return nums

    def check_if_possible(self, x: int, y: int, n: int) -> bool:
        # Check rows and columns
        for x0 in range(9):
            if self.current[y][x0] == n: return False
        for y0 in range(9):
            if self.current[y0][x] == n: return False
        # Check cubes
        for x0 in range((x // 3) * 3, (x // 3) * 3 + 3):
            for y0 in range((y // 3) * 3, (y // 3) * 3 + 3):
                if self.current[y0][x0] == n: return False
        return True

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(Solver().main())
    print(f"This took {round(perf_counter() - start, 2)}s")
