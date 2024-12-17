inputval = ""
curmap = []
robotrow, robotcol = 0, 0
while True:
    inputval = input()
    if not inputval:
        break

    nrow = []
    for cell in inputval:
        if cell == "#":
            nrow.append("#")
            nrow.append("#")
        if cell == "O":
            nrow.append("[")
            nrow.append("]")
        if cell == ".":
            nrow.append(".")
            nrow.append(".")
        if cell == "@":
            robotrow = len(curmap)
            robotcol = len(nrow)
            nrow.append("@")
            nrow.append(".")
    curmap.append(nrow)
print(curmap)
dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}
def try_push(row, col, d):
    if curmap[row][col] == "#":
        return False
    if curmap[row][col] == "[" or curmap[row][col] == "]":
        if curmap[row][col] == "]":
            col -= 1
        if d == "^" or d == "v":
            return try_push(row + dirs[d][0], col, d) and try_push(row + dirs[d][0], col + 1, d)
        elif d == "<":
            return try_push(row, col - 1, d)
        else:
            return try_push(row, col + 2, d)
    return True
def do_push(row, col, d):
    if curmap[row][col] == "#":
        return False
    if curmap[row][col] == "[" or curmap[row][col] == "]":
        if curmap[row][col] == "]":
            col -= 1
        if d == "^" or d == "v":
            do_push(row + dirs[d][0], col, d) and do_push(row + dirs[d][0], col + 1, d)
            curmap[row + dirs[d][0]][col] = "["
            curmap[row + dirs[d][0]][col + 1] = "]"
            curmap[row][col] = "."
            curmap[row][col + 1] = "."
        elif d == "<":
            do_push(row, col - 1, d)
            curmap[row][col - 1] = "["
            curmap[row][col] = "]"
            curmap[row][col + 1] = "."
        else:
            do_push(row, col + 2, d)
            curmap[row][col] = "."
            curmap[row][col + 1] = "["
            curmap[row][col + 2] = "]"
    return True
while True:
    robot_lines = input()
    if not robot_lines:
        break
    for d in robot_lines:
        newrow, newcol = robotrow + dirs[d][0], robotcol + dirs[d][1]
        if try_push(newrow, newcol, d):
            do_push(newrow, newcol, d)
            robotrow, robotcol = newrow, newcol
total = 0
for i, row in enumerate(curmap):
    for j, cell in enumerate(row):
        print(cell, end="")
        if cell == "[":
            total += i * 100 + j
    print()
print(total)
