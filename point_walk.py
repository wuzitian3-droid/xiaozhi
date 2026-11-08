# 一个自己走的点：不随机乱跳，只慢慢拐弯。看看走久了会不会有规律。
import random, math

W, H = 61, 31
STEPS = 6000

def run(seed=0, turn=0.22):
    random.seed(seed)
    x, y = W/2.0, H/2.0
    a = random.random() * math.tau
    grid = [[0]*W for _ in range(H)]
    for _ in range(STEPS):
        a += random.gauss(0, turn)
        nx = x + math.cos(a) * 1.2
        ny = y + math.sin(a) * 1.2
        if nx < 0.5 or nx > W-1.5:
            a = math.pi - a
            nx = x + math.cos(a) * 1.2
        if ny < 0.5 or ny > H-1.5:
            a = -a
            ny = y + math.sin(a) * 1.2
        x, y = nx, ny
        grid[int(y)][int(x)] += 1
    return grid

def show(grid):
    ramp = ' .:-=+*#%@'
    mx = max(max(r) for r in grid) or 1
    for row in grid:
        print(''.join(ramp[min(len(ramp)-1, int(v/mx*(len(ramp)-1)*2))] for v in row))

if __name__ == '__main__':
    show(run(turn=0.22))
