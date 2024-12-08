inputval = ""
total = 0
def eval_expr(ins, ops):
    stack = [ins[0]]
    if ins == [11, 6, 16, 20] and ops == ["+", "*", "+"]:
        pass
    for i, val in enumerate(ins[1:]):
        if ops[i] == "*":
            stack.append(stack.pop() * val)
        elif ops[i] == "+":
            stack.append(stack.pop() + val)
        else:
            stack.append(int(str(stack.pop()) + str(val)))
    return sum(stack)
def gen_combination(n):
    result = ["+"] * n
    while True:
        yield result
        idx = n - 1
        while idx >= 0 and result[idx] == "*":
            result[idx] = "+"
            idx -= 1
        if idx < 0:
            break
        if result[idx] == "+":
            result[idx] = "||"
        else:
            result[idx] = "*"
while True:
    inputval = input()
    if not inputval:
        break
    result, rest = inputval.split(":")
    values = list(map(int, rest.strip().split(" ")))
    result = int(result)
    for ops in gen_combination(len(values) - 1):
        if eval_expr(values, ops) == result:
            total += result
            print(result, values, ops)
            break
print(total)
