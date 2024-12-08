import bisect
inputval = ""
columns = []
rows = []
while True:
    inputval = input()
    if not inputval:
        break
    rows.append([])
    for i, cell in enumerate(inputval):
        if i >= len(columns):
            columns.append([])
        if cell == "#":
            rows[-1].append(i)
            columns[i].append(len(rows) - 1)
        elif cell == "^":
            start_row = len(rows) - 1
            start_col = i
visited_cells = set()
cur_row = start_row
cur_col = start_col
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = 0
while cur_row >= 0 and cur_row < len(rows) and cur_col >= 0 and cur_col < len(columns):
    visited_cells.add((cur_row, cur_col))
    new_row = cur_row + dirs[cur_dir][0]
    new_col = cur_col + dirs[cur_dir][1]
    if new_row >= 0 and new_row < len(rows) and new_col >= 0 and new_col < len(columns) and new_col in rows[new_row]:
        cur_dir = (cur_dir + 1) % 4
        continue
    cur_row = new_row
    cur_col = new_col
print("P1: ", len(visited_cells))
total = 0
def validate_loop():
    cur_row = start_row
    cur_col = start_col
    cur_dir = 0
    visited = set()
    while (cur_row, cur_col, cur_dir) not in visited:
        visited.add((cur_row, cur_col, cur_dir))
        if cur_dir == 0 or cur_dir == 2:
            new_row = bisect.bisect(columns[cur_col], cur_row)
            if cur_dir == 0:
                new_row -= 1
            if new_row < 0 or new_row >= len(columns[cur_col]):
                return False # Escape
            if cur_dir == 0:
                cur_row = columns[cur_col][new_row] + 1
            else:
                cur_row = columns[cur_col][new_row] - 1
        else:
            new_col = bisect.bisect(rows[cur_row], cur_col)
            if cur_dir == 3:
                new_col -= 1
            if new_col < 0 or new_col >= len(rows[cur_row]):
                return False # Escape
            if cur_dir == 1:
                cur_col = rows[cur_row][new_col] - 1
            else:
                cur_col = rows[cur_row][new_col] + 1
        cur_dir = (cur_dir + 1) % 4
    return True
for obs_row, obs_col in visited_cells:
    if obs_row == start_row and obs_col == start_col:
        continue
    bisect.insort(rows[obs_row], obs_col)
    bisect.insort(columns[obs_col], obs_row)
    if validate_loop():
        total += 1
    del rows[obs_row][bisect.bisect_left(rows[obs_row], obs_col)]
    del columns[obs_col][bisect.bisect_left(columns[obs_col], obs_row)]
print("P2: ", total)
