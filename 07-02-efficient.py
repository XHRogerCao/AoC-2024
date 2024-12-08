inputval = ""
total = 0
def eval_expr(target, current, ins, idx):
    if idx == len(ins):
        return target == current
    if current > target:
        return False
    return eval_expr(target, current + ins[idx], ins, idx + 1) or \
        eval_expr(target, current * ins[idx], ins, idx + 1) or \
        eval_expr(target, int(f"{current}{ins[idx]}"), ins, idx + 1)
while True:
    inputval = input()
    if not inputval:
        break
    result, rest = inputval.split(":")
    values = list(map(int, rest.strip().split(" ")))
    result = int(result)
    if eval_expr(result, values[0], values[1:], 0):
        total += result
print(total)
