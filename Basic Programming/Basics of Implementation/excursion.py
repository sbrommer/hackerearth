from math import ceil

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    print(ceil(N / K) + ceil(M / K))
