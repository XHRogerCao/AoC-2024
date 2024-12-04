inputval = ""
input_matrix = []
while True:
    inputval = input()
    if not inputval:
        break
    input_matrix.append(inputval)
total = 0
for i, x in enumerate(input_matrix):
    for j, y in enumerate(x):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx or dy:
                    if i + dx * 3 >= 0 and i + dx * 3 < len(input_matrix) and j + dy * 3 >= 0 and j + dy * 3 < len(x):
                        stofind = "XMAS"
                        for idx, ch in enumerate(stofind):
                            if ch != input_matrix[i + dx * idx][j + dy * idx]:
                                total -= 1
                                break
                        total += 1
print(total)
