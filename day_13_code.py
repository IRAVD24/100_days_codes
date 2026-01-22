from collections import Counter

# number of shoes
X = int(input())

# list of shoe sizes
shoe_sizes = list(map(int, input().split()))

# create Counter
inventory = Counter(shoe_sizes)

# number of customers
N = int(input())

total_earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    
    if inventory[size] > 0:
        total_earnings += price
        inventory[size] -= 1

print(total_earnings)
