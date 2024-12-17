inputval = ""
curmap = []
robotrow, robotcol = 0, 0
while True:
    inputval = input()
    if not inputval:
        break
    curmap.append(list(inputval))
    if "@" in curmap[-1]:
        robotrow = len(curmap) - 1
        robotcol = curmap[-1].index("@")
print(curmap)
dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}
while True:
    robot_lines = input()
    if not robot_lines:
        break
    for d in robot_lines:
        newrow, newcol = robotrow + dirs[d][0], robotcol + dirs[d][1]
        if curmap[newrow][newcol] == "O":
            emptyrow, emptycol = newrow, newcol
            while curmap[emptyrow][emptycol] == "O":
                emptyrow, emptycol = emptyrow + dirs[d][0], emptycol + dirs[d][1]
            if curmap[emptyrow][emptycol] == "#":
                continue
            curmap[emptyrow][emptycol] = "O"
            curmap[newrow][newcol] = "."
        if curmap[newrow][newcol] != "O" and curmap[newrow][newcol] != "#":
            robotrow, robotcol = newrow, newcol
total = 0
for i, row in enumerate(curmap):
    for j, cell in enumerate(row):
        print(cell, end="")
        if cell == "O":
            total += i * 100 + j
    print()
print(total)
