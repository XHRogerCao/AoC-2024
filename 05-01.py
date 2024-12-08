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
    if correct:
        print(ival)
        total += int(ival [len(ival )// 2])
print(total)
