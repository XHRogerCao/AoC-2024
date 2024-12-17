from heapq import heappush, heappop
inputval = ""
curmap = []
deerrow, deercol = 0, 0
endrow, endcol = 0, 0
while True:
    inputval = input()
    if not inputval:
        break
    curmap.append(inputval)
    if "S" in inputval:
        deerrow = len(curmap) - 1
        deercol = inputval.index("S")
    if "E" in inputval:
        endrow = len(curmap) - 1
        endcol = inputval.index("E")
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
visited = {
    # (deerrow, deercol, 3): 0
}
pqueue = [(0, deerrow, deercol, 3)]
minscore = None
while pqueue:
    score, row, col, d = heappop(pqueue)
    if minscore and score > minscore:
        break
    if (row, col, d) not in visited:
        visited[(row, col, d)] = score
        if curmap[row][col] == "E":
            if not minscore:
                minscore = score
                continue
        nrow, ncol = row + dirs[d][0], col + dirs[d][1]
        if curmap[nrow][ncol] != "#":
            heappush(pqueue, (score + 1, nrow, ncol, d))
        heappush(pqueue, (score + 1000, row, col, (d + 1) % 4))
        heappush(pqueue, (score + 1000, row, col, (d - 1) % 4))
marked = set()
def back_mark(row, col, d, distance):
    if (row, col, d) not in visited or visited[(row, col, d)] != distance:
        return
    marked.add((row, col))
    back_mark(row, col, (d + 1) % 4, distance - 1000)
    back_mark(row, col, (d - 1) % 4, distance - 1000)
    back_mark(row - dirs[d][0], col - dirs[d][1], d, distance - 1)

for i in range(4):
    back_mark(endrow, endcol, i, minscore)
print(len(marked))
