import re
from math import gcd
inputval = ""
total = 0
equal_count = 0
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
    Px += 10000000000000
    Py += 10000000000000
    if Px == Py:
        equal_count += 1
    min_tokens = None
    maxA = Px // Adx
    found_min = False
    if Adx * Bdy == Ady * Bdx:
        if Adx * Py == Ady * Px:
            for i in range(maxA + 1):
                j = (Px - Adx * i) // Bdx
                if i * Adx + j * Bdx == Px and i * Ady + j * Bdy == Py:
                    token_count = 3 * i + j
                    if min_tokens is None:
                        min_tokens = token_count
                    else:
                        if min_tokens <= token_count:
                            found_min = True
                        break
            if min_tokens:
                for i in range(maxA, -1, -1):
                    j = (Px - Adx * i) // Bdx
                    if i * Adx + j * Bdx == Px and i * Ady + j * Bdy == Py:
                        token_count = 3 * i + j
                        min_tokens = token_count
                        break
    else:
        j = (Py * Adx - Px * Ady) // (Bdy * Adx - Bdx * Ady)
        i = (Px - Bdx * j) // Adx
        if i * Adx + j * Bdx == Px and i * Ady + j * Bdy == Py:
            token_count = 3 * i + j
            if min_tokens is None:
                min_tokens = token_count
    if min_tokens:
        total += min_tokens
print(total, equal_count)
