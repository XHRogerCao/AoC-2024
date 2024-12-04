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
        if i >= 1 and i < len(input_matrix) - 1 and j >= 1 and j < len(x) - 1:
            foundA = True
            foundB = True
            foundA = (input_matrix[i - 1][j - 1] == "M" and input_matrix[i][j] == "A" and input_matrix[i + 1][j + 1] == "S") or (input_matrix[i - 1][j - 1] == "S" and input_matrix[i][j] == "A" and input_matrix[i + 1][j + 1] == "M")
            foundB = (input_matrix[i - 1][j + 1] == "M" and input_matrix[i][j] == "A" and input_matrix[i + 1][j - 1] == "S") or (input_matrix[i - 1][j + 1] == "S" and input_matrix[i][j] == "A" and input_matrix[i + 1][j - 1] == "M")
            if foundA and foundB:
                total += 1
print(total)
