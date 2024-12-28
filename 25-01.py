from itertools import product
locks = []
keys = []
tot_len = None
while True:
    types = []
    while True:
        inputval = input()
        if not inputval:
            break
        types.append(inputval)
    if not types:
        break
    tot_len = len(types)
    is_key = False
    sums = [0] * len(types[0])
    for i in range(len(types[0])):
        for j in range(len(types)):
            if types[j][i] == "#":
                sums[i] += 1
            elif j == 0:
                is_key = True
    if is_key:
        keys.append(sums)
    else:
        locks.append(sums)
total = 0
for lock, key in product(locks, keys):
    for a, b in zip(lock, key):
        if a + b > tot_len:
            total -= 1
            break
    total += 1
print(total)
