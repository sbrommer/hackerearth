N = int(input())
s = int(input())
f = int(input())
C = list(map(int, input().split()))

i, j = sorted([s - 1, f - 1])

print(min(sum(C[i:j]), sum(C[:i]) + sum(C[j:])))
