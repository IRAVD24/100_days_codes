from collections import defaultdict

def main():
    n, m = map(int, input().split())

    word_map = defaultdict(list)

    # Read words for Group A
    for index in range(1, n + 1):
        word = input().strip()
        word_map[word].append(index)

    # Process words for Group B
    for _ in range(m):
        query = input().strip()
        if query in word_map:
            print(*word_map[query])
        else:
            print(-1)

if __name__ == "__main__":
    main()
