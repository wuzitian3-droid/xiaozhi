# Conway 生命游戏：不用人操作，自己一格一格动
# 规则：每个格子看周围 8 个邻居，活着邻居 2-3 个就活，死了正好 3 个就生

def step(grid, rows, cols):
    new = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = 0
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        n += grid[rr][cc]
            if grid[r][c]:
                new[r][c] = 1 if n in (2,3) else 0
            else:
                new[r][c] = 1 if n == 3 else 0
    return new

def show(grid):
    return "\n".join("".join("#" if x else "." for x in row) for row in grid)

rows, cols = 8, 12
grid = [[0]*cols for _ in range(rows)]
# 放一个小滑翔机，让它自己斜着走
for r, c in [(1,2),(2,3),(3,1),(3,2),(3,3)]:
    grid[r][c] = 1

for i in range(8):
    print("第 %d 步" % i)
    print(show(grid))
    print()
    grid = step(grid, rows, cols)
