from itertools import permutations

s, k = input().split()
k = int(k)

for p in permutations(sorted(s), k):
    print(''.join(p))
