import re
inputval = ""
count = 0
total = 0
enabled = True
while True:
    inputval = input()
    if not inputval:
        break
    valids = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", inputval)

    for inval in valids:
        if inval == "do()":
            enabled = True
        elif inval == "don't()":
            enabled = False
        elif enabled:
            a, b = re.findall("\d{1,3}", inval)
            total += int(a) * int(b)
print(total)
