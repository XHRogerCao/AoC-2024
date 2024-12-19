

registers = []
for i in range(3):
    registers.append(int(input().split(": ")[1]))
input()
program = list(map(int, input().split(": ")[1].split(",")))
min_val = None
def find_val(a, program):
# for val in reversed(program):
    # foundb = False
    global min_val
    print(oct(a))
    if not program:
        if not min_val:
            min_val = a
        else:
            min_val = min(min_val, a)
        return
    for i in range(8):
        b = i
        b = b ^ 3
        c = (a * 8 + i) // (2 ** b)
        b = b ^ 5 ^ c
        if b % 8 == program[-1]:
            find_val(a * 8 + i, program[:-1])
print(find_val(0, program))
print(min_val)
