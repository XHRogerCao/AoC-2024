inputval = input()
cells = []
curid = 0
cur_pos = 0
for i, digit in enumerate(inputval):
    if i % 2 == 0:
        new_pos = cur_pos + int(digit)
        cells.append((int(digit), curid))
        cur_pos = new_pos
        curid += 1
    else:
        new_pos = cur_pos + int(digit)
        cells.append((int(digit), -1))
        cur_pos = new_pos
curid -= 1
cur_index = len(cells) - 1
while cur_index > 0:
    if cells[cur_index][1] != curid:
        cur_index -= 1
        continue
    for idx in range(cur_index):
        if cells[idx][1] == -1 and cells[cur_index][0] <= cells[idx][0]:
            if cells[cur_index][0] == cells[idx][0]:
                cells[idx] = cells[cur_index]
                cells[cur_index] = (cells[cur_index][0], -1)
            else:
                delta = cells[idx][0] - cells[cur_index][0]
                cells[idx] = cells[cur_index]
                cells[cur_index] = (cells[cur_index][0], -1)
                cells.insert(idx + 1, (delta, -1))
                cur_index += 1
            break
    curid -= 1
total = 0
idx = 0
for size, curid in cells:
    if curid != -1:
        total += (idx + idx + size - 1) * size // 2 * curid
    idx += size
print(total)
