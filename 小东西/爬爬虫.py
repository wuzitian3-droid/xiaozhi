import time, sys, math

# 一条会自己爬的小东西：正弦轨迹往前爬，尾巴拖一点
w, h = 60, 12
n = 18
for t in range(160):
    body = [ (int(w*0.15 + (w*0.7)*i/(n-1)),
              int(h/2 + 3.5*math.sin(i*0.55 - t*0.35))) for i in range(n) ]
    grid = [[' ']*w for _ in range(h)]
    for idx,(x,y) in enumerate(body):
        if 0 <= x < w and 0 <= y < h:
            grid[y][x] = '@' if idx==0 else ('o' if idx < n//2 else '.')
    sys.stdout.write('\x1b[H\x1b[J')
    sys.stdout.write('\n'.join(''.join(r) for r in grid))
    sys.stdout.write('\n  t=%d   爬爬虫\n' % t)
    sys.stdout.flush()
    time.sleep(0.08)
