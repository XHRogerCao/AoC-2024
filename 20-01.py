from collections import deque
inputval = ""
curmap = []
while True:
    inputval = input()
    if not inputval:
        break
    curmap.append(list(inputval))
    if "S" in inputval:
        srow, scol = len(curmap) - 1, inputval.index("S")
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs():
    score = {
        (srow, scol, 0): 0
    }
    bfs_queue = deque()
    bfs_queue.append((srow, scol, 0))
    while bfs_queue:
        row, col, coli = bfs_queue.popleft()
        for drow, dcol in dirs:
            nrow, ncol = row + drow, col + dcol
            if nrow >= 0 and nrow < len(curmap) and ncol >= 0 and ncol < len(curmap[0]):
                if (nrow, ncol, coli) not in score and curmap[nrow][ncol] != "#":
                    score[(nrow, ncol, coli)] = score[(row, col, coli)] + 1
                    bfs_queue.append((nrow, ncol, coli))
                else:
                    continue
                if curmap[nrow][ncol] == "E":
                    return score[(nrow, ncol, coli)], score
normal_score, normal_map = bfs()
total = 0
threshold = 100
for i in range(1, len(curmap) - 1):
    for j in range(1, len(curmap[0]) - 1):
        if curmap[i][j] == "#":
            mins = 999999
            maxs = 0
            for drow, dcol in dirs:
                if (i + drow, j + dcol, 0) in normal_map:
                    mins = min(mins, normal_map[(i + drow, j + dcol, 0)])
                    maxs = max(maxs, normal_map[(i + drow, j + dcol, 0)])
            if maxs - mins >= threshold:
                curmap[i][j] = "."
                if normal_score - bfs()[0] >= threshold:
                    total += 1
                curmap[i][j] = "#"
print(total)
