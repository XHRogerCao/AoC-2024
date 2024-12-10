from collections import deque
inputval = ""
topomap = []
while True:
    inputval = input()
    if not inputval:
        break
    topomap.append(inputval)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
total = 0
for i, row in enumerate(topomap):
    for j, cell in enumerate(row):
        if cell == "0":
            bfs_nodes = deque()
            bfs_nodes.append((i, j))
            visited = set()
            while bfs_nodes:
                x, y = bfs_nodes.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if int(topomap[x][y]) == 9:
                    total += 1
                    continue
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < len(topomap) and ny >= 0 and ny < len(topomap[0]):
                        if int(topomap[nx][ny]) - int(topomap[x][y]) == 1:
                            bfs_nodes.append((nx, ny))
print(total)
