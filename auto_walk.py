import random

W, H = 48, 22
grid = [[0]*W for _ in range(H)]
x, y = W//2, H//2
d = random.choice([(1,0),(-1,0),(0,1),(0,-1)])

for step in range(6000):
    grid[y][x] += 1
    # 有惯性：大概率继续走，小概率拐弯
    if random.random() < 0.12:
        if d[0]:
            d = random.choice([(0,1),(0,-1)])
        else:
            d = random.choice([(1,0),(-1,0)])
    nx, ny = x + d[0], y + d[1]
    if 0 <= nx < W and 0 <= ny < H:
        x, y = nx, ny
    else:
        d = (-d[0], -d[1])
        x, y = x + d[0], y + d[1]

mx = max(max(r) for r in grid)
chars = " .:-=+*#%@"
for row in grid:
    print("".join(chars[min(9, v * 10 // (mx + 1))] for v in row))
print("max visits:", mx)
