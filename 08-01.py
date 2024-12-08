inputval = ""
map_col = 0
map_row = 0
antennas = {}
while True:
    inputval = input()
    if not inputval:
        break
    map_col = len(inputval)
    for i, val in enumerate(inputval):
        if val != ".":
            if val not in antennas:
                antennas[val] = []
            antennas[val].append((map_row, i))
    map_row += 1
locations = set()
for freq in antennas:
    for ax, ay in antennas[freq]:
        for bx, by in antennas[freq]:
            if ax == bx and ay == by:
                continue
            cx = bx + (bx - ax)
            cy = by + (by - ay)
            if cx >= 0 and cx < map_row and cy >= 0 and cy < map_col:
                locations.add((cx, cy))
print(len(locations))
