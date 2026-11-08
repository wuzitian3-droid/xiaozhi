# 小东西：一个自己会动的小点
# 跑法：python 摊子/little_life.py   （Ctrl+C 停）
import os, sys, time, math

W, H = 40, 14
if len(sys.argv) > 2:
    W, H = int(sys.argv[1]), int(sys.argv[2])

def frame(t):
    # 一个点在里头弹，撞墙就弹回来；顺带呼吸（亮度按 sin 变）
    x = (W - 1) * abs(((t * 0.9) % 2) - 1)
    y = (H - 1) * abs(((t * 0.37) % 2) - 1)
    bright = 0.5 + 0.5 * math.sin(t * 0.3)
    ch = "@" if bright > 0.66 else ("O" if bright > 0.33 else ".")
    rows = []
    for j in range(H):
        row = []
        for i in range(W):
            if i == 0 or i == W - 1 or j == 0 or j == H - 1:
                row.append("#")
            elif int(round(x)) == i and int(round(y)) == j:
                row.append(ch)
            else:
                row.append(" ")
        rows.append("".join(row))
    return "\n".join(rows)

try:
    t = 0.0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame(t))
        print(f"t={t:.1f}  Ctrl+C 停")
        time.sleep(0.08)
        t += 0.1
except KeyboardInterrupt:
    print("\n停了。")
