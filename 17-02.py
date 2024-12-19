registers = []
for i in range(3):
    registers.append(int(input().split(": ")[1]))
input()
program = list(map(int, input().split(": ")[1].split(",")))
inst_ptr = 0
def get_combo(data):
    if data >= 4 and data <= 6:
        return registers[data - 4]
    return data
new_prog = []
init_vals = [0, registers[1], registers[2]]
while len(new_prog) != len(program) or not all(map(lambda a: a[0] == a[1], zip(new_prog, program))):
    init_vals[0] += 1
    registers = [init_vals[0], init_vals[1], init_vals[2]]
    new_prog = []
    inst_ptr = 0
    if init_vals[0] == 117440:
        pass
    while inst_ptr >= 0 and inst_ptr < len(program):
        jumped = False
        op = program[inst_ptr]
        data = program[inst_ptr + 1]
        if op == 0:
            registers[0] = registers[0] // (2 ** get_combo(data))
        elif op == 1:
            registers[1] ^= data
        elif op == 2:
            registers[1] = get_combo(data) % 8
        elif op == 3:
            if registers[0]:
                inst_ptr = data
                jumped = True
        elif op == 4:
            registers[1] ^= registers[2]
        elif op == 5:
            new_prog.append(get_combo(data) % 8)
            if len(new_prog) > len(program) or new_prog[-1] != program[len(new_prog) - 1]:
                break
        elif op == 6:
            registers[1] = registers[0] // (2 ** get_combo(data))
        elif op == 7:
            registers[2] = registers[0] // (2 ** get_combo(data))
        if not jumped:
            inst_ptr += 2

print(f"Registers:{init_vals[0]}")
