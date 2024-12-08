from heapq import heapify, heappop, heappush
inputval = ""
input_matrix = []
suffixes = {}
exists = set()
while True:
    inputval = input()
    if not inputval:
        break
    a, b = inputval.split("|")
    if a not in suffixes:
        suffixes[a] = []
    suffixes[a].append(b)
    exists.add(a)
    exists.add(b)
total = 0
while True:
    inputval = input()
    if not inputval:
        break
isTotal = True
for a in exists:
    for b in exists:
        if a == b: continue
        if (a in suffixes and b in suffixes[a]) or (b in suffixes and a in suffixes[b]):
            pass
        else:
            isTotal = False
print(isTotal)
