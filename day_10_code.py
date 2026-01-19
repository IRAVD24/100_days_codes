k = int(input().strip())
rooms = list(map(int, input().strip().split()))

counts = {}
for r in rooms:
    counts[r] = counts.get(r, 0) + 1

for room, count in counts.items():
    if count == 1:
        print(room)
        break
