from functools import cache
inputval = ""
patterns =[]
while True:
    inputval = input()
    if not inputval:
        break
    patterns += inputval.split(", ")
total = 0
input()
@cache
def is_possible(inval):
    if not inval:
        return 1
    score = 0
    for pattern in patterns:
        if len(pattern) <= len(inval) and pattern == inval[:len(pattern)]:
            score += is_possible(inval[len(pattern):])

    return score
while True:
    inputval = input()
    if not inputval:
        break
    total += is_possible(inputval)
print(total)
