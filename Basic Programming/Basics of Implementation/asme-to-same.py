from collections import Counter

T = int(input())

for _ in range(T):
    input()
    s = Counter(filter(lambda c: c.isalpha(), input()))
    t = Counter(input())

    print('Yes' if all(n <= t[k] for k, n in s.items()) else 'No')
