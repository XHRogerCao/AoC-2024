wires = {}
while True:
    inputval = input()
    if not inputval:
        break
    inputs, val = inputval.split(": ")
    wires[inputs] = int(val)
wires_to_check = list(wires.keys())

connections = {}
dependencies = {}

while True:
    inputval = input()
    if not inputval:
        break
    a1, op, a2, ar, res = inputval.split(" ")
    connections[(a1, a2, op, res)] = [a1, a2]
    if a1 not in dependencies:
        dependencies[a1] = []
    dependencies[a1].append((a1, a2, op, res))
    if a2 not in dependencies:
        dependencies[a2] = []
    dependencies[a2].append((a1, a2, op, res))

while wires_to_check:
    top = wires_to_check.pop()
    if top not in dependencies:
        continue
    for dep in dependencies[top]:
        connections[dep].remove(top)
        if not connections[dep]:
            a1, a2, op, res = dep
            if op == "AND":
                wires[res] = wires[a1] & wires[a2]
            elif op == "OR":
                wires[res] = wires[a1] | wires[a2]
            elif op == "XOR":
                wires[res] = wires[a1] ^ wires[a2]
            wires_to_check.append(res)
i = 0
val = 0
for idx in sorted(wires.keys()):
    print(idx, wires[idx])
while f"z{i:02}" in wires:
    val += (2 ** i) * wires[f"z{i:02}"]
    i += 1
print(val)
