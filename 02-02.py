inputval = ""
count = 0
def get_safety(inputs):
    isAscend = None
    for a0, a1 in zip(inputs[:-1], inputs[1:]):
        if isAscend is None:
            if a0 < a1:
                isAscend = True
            else:
                isAscend = False
        else:
            if (a0 < a1) != isAscend:
                return False
        if abs(a0 - a1) < 1 or abs(a0 - a1) > 3:
            return False
    return True
while True:
    inputval = input()
    if not inputval:
        break
    inputs = list(map(int, inputval.split()))
    if get_safety(inputs):
        count += 1
    else:
        for i, data in enumerate(inputs):
            newinput = inputs[:i] + inputs[i + 1:]
            if get_safety(newinput):
                count += 1
                break
print(count)
