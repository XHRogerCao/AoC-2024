connections = {}
total = 0
while True:
    inputval = input()
    if not inputval:
        break
    to, fr = inputval.split("-")
    if to not in connections:
        connections[to] = set()
    if fr not in connections:
        connections[fr] = set()
    connections[to].add(fr)
    connections[fr].add(to)
    all_ints = connections[to].intersection(connections[fr])
    for common in all_ints:
        if to[0] == "t" or fr[0] == "t" or common[0] == "t":
            total += 1
print(total)
