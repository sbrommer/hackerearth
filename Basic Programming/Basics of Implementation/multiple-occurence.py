T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ix = dict()
    s = 0
    for i, a in enumerate(A):
        if a in ix:
            s += i - ix[a]
        ix[a] = i
    print(s)
