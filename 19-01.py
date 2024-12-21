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
        return True
    for pattern in patterns:
        if len(pattern) <= len(inval) and pattern == inval[:len(pattern)]:
            if is_possible(inval[len(pattern):]):
                return True
    return False
while True:
    inputval = input()
    if not inputval:
        break
    total += 1 if is_possible(inputval) else 0
print(total)
