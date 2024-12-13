from collections import deque
inputval = ""
plot_map = []
while True:
    inputval = input()
    if not inputval:
        break
    plot_map.append(list(inputval))
total = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i, row in enumerate(plot_map):
    for j, cell in enumerate(row):
        if plot_map[i][j]:
            first_cell = plot_map[i][j]
            visited = set()
            perimeter = 0
            bfs_queue = deque()
            bfs_queue.append((i, j))
            while bfs_queue:
                ti, tj = bfs_queue.popleft()
                if (ti, tj) not in visited:
                    visited.add((ti, tj))
                    plot_map[ti][tj] = ""
                    for dx, dy in dirs:
                        ni, nj = ti + dx, tj + dy
                        if ni < 0 or ni >= len(plot_map) or nj < 0 or nj >= len(plot_map[0]):
                            perimeter += 1
                        elif plot_map[ni][nj] != first_cell:
                            if (ni, nj) not in visited:
                                perimeter += 1
                        else:
                            bfs_queue.append((ni, nj))
            print(len(visited) * perimeter)
            total += len(visited) * perimeter
print(total)
