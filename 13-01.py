import re
inputval = ""
total = 0
while True:
    inputval = input()
    if not inputval:
        break
    inputvalb = input()
    prizein = input()
    input()
    Adx, Ady = tuple(map(int, re.match(r"Button A: X\+([0-9]+), Y\+([0-9]+)", inputval).group(1, 2)))
    Bdx, Bdy = tuple(map(int, re.match(r"Button B: X\+([0-9]+), Y\+([0-9]+)", inputvalb).group(1, 2)))
    Px, Py = tuple(map(int, re.match(r"Prize: X=([0-9]+), Y=([0-9]+)", prizein).group(1, 2)))
    min_tokens = None
    maxA = Px // Adx
    for i in range(maxA, -1, -1):
        j = (Px - Adx * i) // Bdx
        if i * Adx + j * Bdx == Px and i * Ady + j * Bdy == Py:
            token_count = 3 * i + j
            if min_tokens is None:
                min_tokens = token_count
            else:
                min_tokens = min(min_tokens, token_count)
    if min_tokens:
        total += min_tokens
print(total)
