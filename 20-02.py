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
    if "E" in inputval:
        erow, ecol = len(curmap) - 1, inputval.index("E")
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(srow, scol, erow, ecol):
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
                if (nrow, ncol) == (erow, ecol):
                    return score[(nrow, ncol, coli)], score
normal_score, normal_map = bfs(srow, scol, erow, ecol)
reverse_score, reverse_map = bfs( erow, ecol, srow, scol,)
total = 0
threshold = int(input())
cheat_range = 20
timesaves = {}
for i in range(1, len(curmap) - 1):
    for j in range(1, len(curmap[0]) - 1):
        if curmap[i][j] != "#":
            for di in range(-cheat_range, cheat_range + 1):
                for dj in range(-cheat_range, cheat_range + 1):
                    ni, nj = i + di, j + dj
                    if abs(di) + abs(dj) > cheat_range:
                        continue
                    if ni < 0 or ni >= len(curmap) or nj < 0 or nj >= len(curmap[0]):
                        continue
                    if curmap[ni][nj] == "#":
                        continue
                    score = normal_map[(i, j, 0)] + reverse_map[(ni, nj, 0)] + abs(di) + abs(dj)
                    if normal_score - score >= threshold:
                        total += 1
                        timesaves[normal_score - score] = timesaves.get(normal_score - score, 0) + 1
print(total, timesaves)
