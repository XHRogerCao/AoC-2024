inputval = ""
count = 0
while True:
    inputval = input()
    if not inputval:
        break
    inputs = list(map(int, inputval.split()))
    isAscend = None
    for a0, a1 in zip(inputs[:-1], inputs[1:]):
        if isAscend is None:
            if a0 < a1:
                isAscend = True
            else:
                isAscend = False
        else:
            if (a0 < a1) != isAscend:
                count -= 1
                break
        if abs(a0 - a1) < 1 or abs(a0 - a1) > 3:
            count -= 1
            break
    count += 1
print(count)
