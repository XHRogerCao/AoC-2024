from collections import deque
inputval = ""
falling_bytes = []
while True:
    inputval = input()
    if not inputval:
        break
    falling_bytes.append(tuple(map(int, inputval.split(","))))
visited = {
    (0, 0): 0
}
bfs_queue = deque()
bfs_queue.append((0, 0))
obstacles = set(falling_bytes)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
mapsize = 70
union_set = []
def find_ancestor(row, col):
    if union_set[row][col] != (row, col):
        union_set[row][col] = find_ancestor(union_set[row][col][0], union_set[row][col][1])
    return union_set[row][col]
def union_sets(row1, col1, row2, col2):
    ansrow, anscol = find_ancestor(row1, col1)
    union_set[ansrow][anscol] = find_ancestor(row2, col2)
for i in range(mapsize + 1):
    union_set.append([])
    for j in range(mapsize + 1):
        union_set[-1].append((i, j))
for i in range(mapsize + 1):
    for j in range(mapsize + 1):
        if (i, j) not in obstacles:
            for drow, dcol in dirs:
                nrow, ncol = i + drow, j + dcol
                if nrow >= 0 and nrow <= mapsize and ncol >= 0 and ncol <= mapsize:
                    if (nrow, ncol) not in obstacles:
                        union_sets(i, j, nrow, ncol)
for row, col in reversed(falling_bytes):
    obstacles.remove((row, col))
    for drow, dcol in dirs:
        nrow, ncol = row + drow, col + dcol
        if nrow >= 0 and nrow <= mapsize and ncol >= 0 and ncol <= mapsize:
            if (nrow, ncol) not in obstacles:
                union_sets(row, col, nrow, ncol)
                if find_ancestor(0, 0) == find_ancestor(mapsize, mapsize):
                    print(row, col)
                    exit(0)
