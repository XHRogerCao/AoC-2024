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
obstacles = set(falling_bytes[:min(len(falling_bytes), 1024)])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
mapsize = 70
while bfs_queue:
    row, col = bfs_queue.popleft()
    for drow, dcol in dirs:
        nrow, ncol = row + drow, col + dcol
        if nrow >= 0 and nrow <= mapsize and ncol >= 0 and ncol <= mapsize:
            if (nrow, ncol) not in obstacles and (nrow, ncol) not in visited:
                visited[(nrow, ncol)] = visited[(row, col)] + 1
                bfs_queue.append((nrow, ncol))
                if nrow == mapsize and ncol == mapsize:
                    print(visited[(nrow, ncol)])
                    exit(0)
