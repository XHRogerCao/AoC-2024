from collections import Counter
stones = Counter(input().split())
for i in range(75):
    new_stones = Counter()
    for stone in stones:
        if stone == "0":
            new_stones["1"] = new_stones.get("1", 0) + stones["0"]
        elif len(stone) % 2 == 0:
            lside = str(int(stone[:len(stone) // 2]))
            rside = str(int(stone[len(stone) // 2:]))
            new_stones[lside] = new_stones.get(lside, 0) + stones[stone]
            new_stones[rside] = new_stones.get(rside, 0) + stones[stone]
        else:
            rside = str(2024 * int(stone))
            new_stones[rside] = new_stones.get(rside, 0) + stones[stone]
    stones = new_stones
    print(i)
total = 0
for stone in stones:
    total += stones[stone]
print(total)
