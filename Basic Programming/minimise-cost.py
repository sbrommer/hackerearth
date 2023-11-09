def readints():
    return list(map(int, input().split()))


N, K = readints()
A = readints()

p, n = 0, 0

while p < N and n < N:
    if A[n] < 0 < A[p] and abs(p - n) <= K:
        d = min(A[p], abs(A[n]))
        A[p] -= d
        A[n] += d

    if A[n] >= 0:
        n += 1
    elif A[p] <= 0:
        p += 1
    elif n < p:
        n += 1
    else:
        p += 1

print(sum(map(abs, A)))
