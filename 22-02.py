from functools import cache
inputval = ""
magic = 16777216
@cache
def generate(num):
    v1 = ((num * 64) ^ num) % magic
    v2 = ((v1 // 32) ^ v1) % magic
    v3 = ((v2 * 2048) ^ v2) % magic
    return v3
total = 0
possible_deltas = set()
all_prices = []
every_price = {}
while True:
    inputval = input()
    if not inputval:
        break
    sval = int(inputval)
    price = int(inputval[-1])
    price_deltas = []
    prices = []
    for i in range(2000):
        nsval = generate(sval)
        nprice = int(str(nsval)[-1])
        prices.append(nprice)
        price_deltas.append(nprice - price)
        # if i < 10:
        #     print(nprice, nprice - price)
        sval = nsval
        price = nprice
    max_banana = {}
    max_v = 0
    for i in range(1997):
        deltas = tuple(price_deltas[i:i+4])
        if deltas not in max_banana:
            max_banana[deltas] = prices[i+3]
            possible_deltas.add(deltas)
            every_price[deltas] = every_price.get(deltas, 0) + prices[i+3]
maxval = 0
for deltas in every_price:
    maxval = max(maxval, every_price[deltas])
print(maxval)
