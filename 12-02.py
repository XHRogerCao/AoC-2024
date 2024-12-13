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
            bfs_queue = deque()
            bfs_queue.append((i, j))
            minx, miny, maxx, maxy = i, j, i, j
            while bfs_queue:
                ti, tj = bfs_queue.popleft()
                if (ti, tj) not in visited:
                    visited.add((ti, tj))
                    minx = min(minx, ti)
                    maxx = max(maxx, ti)
                    miny = min(miny, tj)
                    maxy = max(maxy, tj)

                    plot_map[ti][tj] = ""
                    for dx, dy in dirs:
                        ni, nj = ti + dx, tj + dy
                        if ni < 0 or ni >= len(plot_map) or nj < 0 or nj >= len(plot_map[0]):
                            pass
                        elif plot_map[ni][nj] != first_cell:
                            pass
                        else:
                            bfs_queue.append((ni, nj))
            sides = 0
            # Top side
            for scani in range(minx, maxx + 1):
                is_edge = False
                for scanj in range(miny, maxy + 1):
                    if (scani, scanj) in visited and (scani - 1, scanj) not in visited:
                        if not is_edge:
                            sides += 1
                        is_edge = True
                    else:
                        is_edge = False
            # Bottom side
            for scani in range(minx, maxx + 1):
                is_edge = False
                for scanj in range(miny, maxy + 1):
                    if (scani, scanj) in visited and (scani + 1, scanj) not in visited:
                        if not is_edge:
                            sides += 1
                        is_edge = True
                    else:
                        is_edge = False
            # Left side
            for scanj in range(miny, maxy + 1):
                is_edge = False
                for scani in range(minx, maxx + 1):
                    if (scani, scanj) in visited and (scani, scanj - 1) not in visited:
                        if not is_edge:
                            sides += 1
                        is_edge = True
                    else:
                        is_edge = False
            # Right side
            for scanj in range(miny, maxy + 1):
                is_edge = False
                for scani in range(minx, maxx + 1):
                    if (scani, scanj) in visited and (scani, scanj + 1) not in visited:
                        if not is_edge:
                            sides += 1
                        is_edge = True
                    else:
                        is_edge = False
            print(len(visited) * sides)
            total += len(visited) * sides
print(total)
