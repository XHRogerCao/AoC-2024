inputval = input()
cells = []
curid = 0
for i, digit in enumerate(inputval):
    if i % 2 == 0:
        for _ in range(int(digit)):
            cells.append(curid)
        curid += 1
    else:
        for _ in range(int(digit)):
            cells.append(-1)
overall = []
while cells[-1] == -1:
    cells.pop()
while len(overall) < len(cells):
    if cells[len(overall)] == -1:
        overall.append(cells.pop())
        while cells[-1] == -1:
            cells.pop()
    else:
        overall.append(cells[len(overall)])
total = 0
for i, curid in enumerate(overall):
    total += i * curid
print(total)
