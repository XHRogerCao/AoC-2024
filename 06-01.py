inputval = ""
cur_map = []
while True:
    inputval = input()
    if not inputval:
        break
    cur_line = list(inputval)
    cur_map.append(cur_line)
start_i, start_j = 0, 0
for i, row in enumerate(cur_map):
    for j, cell in enumerate(row):
        if cell == "^":
            start_i = i
            start_j = j
print(start_i, start_j)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = 0
while start_i >= 0 and start_i < len(cur_map) and start_j >= 0 and start_j < len(cur_map[0]):
    cur_map[start_i][start_j] = "X"
    newi = start_i + dirs[cur_dir][0]
    newj = start_j + dirs[cur_dir][1]
    if newi >= 0 and newi < len(cur_map) and newj >= 0 and newj < len(cur_map[0]):
        if cur_map[newi][newj] == "#":
            cur_dir = (cur_dir + 1) % 4
            continue
    start_i = newi
    start_j = newj
total = 0
for i, row in enumerate(cur_map):
    for j, cell in enumerate(row):
        print(cell, end="")
        if cell == "X":
            total += 1
    print()
print(total)
