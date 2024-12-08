from heapq import heapify, heappop, heappush
inputval = ""
input_matrix = []
suffixes = {}
while True:
    inputval = input()
    if not inputval:
        break
    a, b = inputval.split("|")
    if a not in suffixes:
        suffixes[a] = []
    suffixes[a].append(b)
total = 0
while True:
    inputval = input()
    if not inputval:
        break
    ival = inputval.split(",")
    correct = True
    for i, val in enumerate(ival):
        for j in range(i, len(ival)):
            if ival[j] in suffixes and val in suffixes[ival[j]]:
                correct = False
                break
        if not correct:
            break
    if not correct:
        hcount = {}
        for id in ival:
            for id2 in ival:
                if id in suffixes and id2 in suffixes[id]:
                    hcount[id2] = hcount.get(id2, 0) + 1
        pq = []
        for id in ival:
            if id not in hcount:
                pq.append(id)
        result = []
        while pq:
            top = pq.pop()
            result.append(top)
            if top in suffixes:
                for suffix in suffixes[top]:
                    if suffix in hcount:
                        hcount[suffix] -= 1
                        if hcount[suffix] == 0:
                            pq.append(suffix)
        total += int(result [len(result )// 2])
print(total)
