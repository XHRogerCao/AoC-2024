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
        print(get_combo(data) % 8, end=",")
    elif op == 6:
        registers[1] = registers[0] // (2 ** get_combo(data))
    elif op == 7:
        registers[2] = registers[0] // (2 ** get_combo(data))
    if not jumped:
        inst_ptr += 2

print(f"Registers:{registers}")
