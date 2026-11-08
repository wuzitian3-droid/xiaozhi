# 会自己动的小东西：康威生命游戏，纯文本跑
import time, random

W, H = 24, 12

def new():
    g = [[0]*W for _ in range(H)]
    # 中间放一个滑翔机，它会自己往右下走
    for dx, dy in [(1,0),(2,1),(0,2),(1,2),(2,2)]:
        g[2+dy][2+dx] = 1
    return g

def step(g):
    n = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            c = sum(g[(y+dy)%H][(x+dx)%W]
                    for dy in (-1,0,1) for dx in (-1,0,1)
                    if (dx,dy) != (0,0))
            n[y][x] = 1 if c == 3 or (c == 2 and g[y][x]) else 0
    return n

def show(g):
    print('\n'.join(''.join('#' if c else '.' for c in row) for row in g))

if __name__ == '__main__':
    g = new()
    for i in range(8):
        show(g)
        print('--- 第%d代' % i)
        g = step(g)
        time.sleep(0.3)
