S = input().strip()

result = -1
for i in range(len(S) - 1):
    if S[i].isalnum() and S[i] == S[i + 1]:
        result = S[i]
        break
print(result)