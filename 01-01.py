inputval = ""
l1 = []
l2 = []
while True:
    inputval = input()
    if not inputval:
        break
    a, b = inputval.split("   ")
    l1.append(int(a))
    l2.append(int(b))
l1.sort()
l2.sort()
total = 0
for a, b in zip(l1, l2):
    total += abs(a - b)
print(total)
