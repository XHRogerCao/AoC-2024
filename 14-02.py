import re
inputval = ""
total = 0
xsize = 101
ysize = 103
deltatime = 100
q1, q2, q3, q4 = 0, 0, 0, 0
robotspos = []
robotsvel = []
while True:
    inputval = input()
    if not inputval:
        break
    px, py, vx, vy = tuple(map(int, re.match(r"p=([0-9]+),([0-9]+) v=(\-?[0-9]+),(\-?[0-9]+)", inputval).group(1, 2, 3, 4)))
    robotspos.append([px, py])
    robotsvel.append((vx, vy))
elapsed = 0
while True:
    elapsed += 1
    curmap = []
    for i in range(ysize):
        curmap.append(["."] * xsize)
    for pos, vel in zip(robotspos, robotsvel):
        pos[0], pos[1] = (pos[0] + vel[0]) % xsize, (pos[1] + vel[1]) % ysize
        curmap[pos[1]][pos[0]] = "#"

    col_count = [0] * xsize
    last_row_empty = True
    cluster_count = 0
    for row_idx, row in enumerate(curmap):
        for idx, cell in enumerate(row):
            if cell == "#":
                col_count[idx] += 1
                if row_idx >= 80 and idx < 25:
                    last_row_empty = False
                is_cluster = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        nrow, ncol = row_idx + i, idx + j
                        if nrow >= 0 and nrow < ysize and ncol >= 0 and ncol < xsize:
                            if curmap[nrow][ncol] == "#":
                                is_cluster += 1
                if is_cluster >= 2:
                    cluster_count += 1
    if cluster_count >= 100:
        print(elapsed)
        for row in curmap:
            for idx, cell in enumerate(row):
                print(cell, end="")
            print()
        print()
        input()
    if elapsed % 1000 == 0:
        print(elapsed)
# print(q1 * q2 * q3 * q4)
