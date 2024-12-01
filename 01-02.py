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
total = 0
for a in l1:
    total += a * l2.count(a)
print(total)
