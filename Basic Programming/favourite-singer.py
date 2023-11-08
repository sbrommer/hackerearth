from collections import Counter

input()

singers = list(map(int, input().split()))
counts = list(Counter(singers).values())
max_count = max(counts)

print(counts.count(max_count))
