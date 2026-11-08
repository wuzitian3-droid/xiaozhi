import random, math, json

# 一个自己走的点：有惯性，会拐弯，走很久
# 不看热闹，看它踩过的地方有没有规律

W, H = 80, 40
x, y = W/2, H/2
a = random.uniform(0, 2*math.pi)  # 朝向
speed = 1.0

grid = [[0]*W for _ in range(H)]

turn_bias = 0.0  # 自己慢慢积累的转弯偏好

for step in range(200000):
    # 每步随机小拐弯 + 一点积累的偏好
    a += random.gauss(0, 0.15) + turn_bias
    turn_bias *= 0.999
    turn_bias += random.gauss(0, 0.002)
    turn_bias = max(-0.05, min(0.05, turn_bias))

    x += math.cos(a)*speed
    y += math.sin(a)*speed

    # 撞墙反弹（不是乱撞，是拐弯）
    if x < 1 or x > W-2:
        a = math.pi - a
        x = max(1, min(W-2, x))
        turn_bias *= 0.5
    if y < 1 or y > H-2:
        a = -a
        y = max(1, min(H-2, y))
        turn_bias *= 0.5

    grid[int(y)][int(x)] += 1

# 出来看看：热的地方在哪儿
flat = [c for row in grid for c in row]
total = sum(flat)
print('总步数', total)
print('空格子', sum(1 for c in flat if c == 0), '/', W*H)
mx = max(flat)
print('最热格子踩了', mx, '次')

# 画个大概轮廓
for row in grid:
    print(''.join('#' if c > mx*0.5 else ('+' if c > mx*0.15 else ('.' if c > 0 else ' ')) for c in row))
