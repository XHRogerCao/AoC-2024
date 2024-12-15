import re
inputval = ""
total = 0
xsize = 101
ysize = 103
deltatime = 100
q1, q2, q3, q4 = 0, 0, 0, 0
while True:
    inputval = input()
    if not inputval:
        break
    px, py, vx, vy = tuple(map(int, re.match(r"p=([0-9]+),([0-9]+) v=(\-?[0-9]+),(\-?[0-9]+)", inputval).group(1, 2, 3, 4)))
    newpx, newpy = (px + vx * deltatime) % xsize, (py + vy * deltatime) % ysize
    if newpx < xsize // 2:
        if newpy < ysize // 2:
            q1 += 1
        elif newpy > ysize // 2:
            q2 += 1
    elif newpx > xsize // 2:
        if newpy < ysize // 2:
            q3 += 1
        elif newpy > ysize // 2:
            q4 += 1
print(q1 * q2 * q3 * q4)
