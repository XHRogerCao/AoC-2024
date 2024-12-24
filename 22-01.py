from functools import cache
inputval = ""
magic = 16777216
@cache
def generate(num):
    v1 = ((num * 64) ^ num) % magic
    v2 = ((v1 // 32) ^ v1) % magic
    v3 = ((v2 * 2048) ^ v2) % magic
    return v3
total = 0
while True:
    inputval = input()
    if not inputval:
        break
    sval = int(inputval)
    for i in range(2000):
        sval = generate(sval)
        # if i < 10:
        #     print(sval)
    total += sval
print(total)
