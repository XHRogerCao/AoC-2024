from itertools import product
import random
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
    dependencies[res] = (a1, a2, op, res)
def validate_deps(max_i, res_id, all_deps):
    all_deps.add(res_id)
    if res_id not in dependencies:
        return int(res_id[1:]) <= max_i
    else:
        return validate_deps(max_i, dependencies[res_id][0], all_deps) and validate_deps(max_i, dependencies[res_id][1], all_deps)
def evaluate(res_id, all_inputs):
    if res_id in all_inputs:
        return all_inputs[res_id]
    else:
        a1, a2, op, res = dependencies[res_id]
        if op == "AND":
            return evaluate(a1, all_inputs) & evaluate(a2, all_inputs)
        elif op == "OR":
            return evaluate(a1, all_inputs) | evaluate(a2, all_inputs)
        elif op == "XOR":
            return evaluate(a1, all_inputs) ^ evaluate(a2, all_inputs)
def validate_add(i):
    try:
        if i > 0:
            if not validate_add(i - 1):
                return False
        for xmax, ymax in product(range(2), range(2)):
            for random_check in range(5):
                all_inputs = {
                    f"x{i:02}": xmax,
                    f"y{i:02}": ymax
                }
                xval = xmax * (2 ** i)
                yval = ymax * (2 ** i)
                for j in range(i):
                    xj = random.choice([0, 1])
                    yj = random.choice([0, 1])
                    xval += xj * (2 ** j)
                    yval += yj * (2 ** j)
                    all_inputs[f"x{j:02}"] = xj
                    all_inputs[f"y{j:02}"] = yj
                zmax = ((xval + yval) >> i) % 2
                if evaluate(f"z{i:02}", all_inputs) != zmax:
                    return False
        return True
    except:
        return False
def exchange_validate(i, set1, set2):
    for id1, id2 in product(set1, set2):
        if id1 == id2:
            continue
        if id1 not in dependencies or id2 not in dependencies:
            continue
        dependencies[id1], dependencies[id2] = dependencies[id2], dependencies[id1]
        res = validate_add(i)
        dependencies[id1], dependencies[id2] = dependencies[id2], dependencies[id1]
        if res:
            return id1, id2
digits = 0
val = 0
for idx in sorted(wires.keys()):
    print(idx, wires[idx])
while f"x{digits:02}" in wires:
    digits += 1
safe_set = set()
new_deps = []
every_deps = []
for i in range(digits):
    all_deps = set()
    if not validate_deps(i, f"z{i:02}", all_deps):
        print(f"z{i:02}")
    all_new_deps = (list(sorted(all_deps.difference(safe_set))))
    print(all_new_deps)
    new_deps.append(all_new_deps)
    every_deps.append(all_deps)
    safe_set.update(all_deps)
for i in range(digits):
    if not validate_add(i):
        print(i)
        break
# print(exchange_validate(10, new_deps[10], new_deps[11]))
# print(exchange_validate(17, new_deps[17], set(dependencies.keys()).difference(every_deps[17]) ))
# print(exchange_validate(35, new_deps[35], set(dependencies.keys()).difference(every_deps[35]) ))
print(exchange_validate(39, new_deps[39], new_deps[40]))
print(val)
