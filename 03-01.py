import re
inputval = ""
count = 0
total = 0
while True:
    inputval = input()
    if not inputval:
        break
    valids = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inputval)

    for a, b in valids:
        total += int(a) * int(b)
print(total)
