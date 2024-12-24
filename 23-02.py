connections = {}
total = 0
best_set = []
while True:
    inputval = input()
    if not inputval:
        break
    to, fr = inputval.split("-")
    if to not in connections:
        connections[to] = set()
    if fr not in connections:
        connections[fr] = set()
    connections[to].add(frozenset((fr,)))
    connections[fr].add(frozenset((to,)))
    prev_ints = None
    all_ints = connections[to].intersection(connections[fr])
    while prev_ints != all_ints:
        if prev_ints:
            pass
        for common in all_ints:
            new_set = [to, fr, *common]
            if len(new_set) > len(best_set):
                best_set = new_set
            connections[to].add(frozenset((fr, *common)))
            connections[fr].add(frozenset((to, *common)))
            for anchor in common:
                connections[anchor].add(frozenset((fr, to, *(common - frozenset((anchor,))))))
        prev_ints = all_ints
        all_ints = connections[to].intersection(connections[fr])
print(",".join(sorted(best_set)))
