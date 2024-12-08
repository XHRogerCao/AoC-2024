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
cur_i, cur_j = start_i, start_j
while cur_i >= 0 and cur_i < len(cur_map) and cur_j >= 0 and cur_j < len(cur_map[0]):
    if cur_map[cur_i][cur_j] != "^":
        cur_map[cur_i][cur_j] = "X"
    newi = cur_i + dirs[cur_dir][0]
    newj = cur_j + dirs[cur_dir][1]
    if newi >= 0 and newi < len(cur_map) and newj >= 0 and newj < len(cur_map[0]):
        if cur_map[newi][newj] == "#":
            cur_dir = (cur_dir + 1) % 4
            continue
    cur_i = newi
    cur_j = newj
possible_obs = []
for i, row in enumerate(cur_map):
    for j, cell in enumerate(row):
        if cell == "X":
            possible_obs.append((i, j))
def validate_loop():
    cur_i, cur_j = start_i, start_j
    cur_dir = 0
    passed_pos = set()
    while cur_i >= 0 and cur_i < len(cur_map) and cur_j >= 0 and cur_j < len(cur_map[0]):
        if (cur_i, cur_j, cur_dir) in passed_pos:
            return True
        passed_pos.add((cur_i, cur_j, cur_dir))
        newi = cur_i + dirs[cur_dir][0]
        newj = cur_j + dirs[cur_dir][1]
        if newi >= 0 and newi < len(cur_map) and newj >= 0 and newj < len(cur_map[0]):
            if cur_map[newi][newj] == "#":
                cur_dir = (cur_dir + 1) % 4
                continue
        cur_i = newi
        cur_j = newj
total = 0
for posi, posj in possible_obs:
    cur_map[posi][posj] = "#"
    if validate_loop():
        total += 1
    cur_map[posi][posj] = "."
print(total)
