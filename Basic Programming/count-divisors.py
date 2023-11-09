l, r, k = map(int, input().split())

print(sum(not i % k for i in range(l, r + 1)))
