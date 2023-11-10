from collections import Counter

T = int(input())

for _ in range(T):
    n = int(input())
    s = input()

    print(sum(c // 2 for c in Counter(s).values()))
