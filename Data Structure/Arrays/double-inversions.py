from operator import add


def is_permutation(A):
    return min(A) == 1 and max(A) == n and len(set(A)) == n


T = int(input())

for _ in range(T):
    n = int(input())
    IA = list(map(int, input().split()))
    IR = list(map(int, input().split()))

    A = [n - add(*z) for z in zip(IA, IR[::-1])]

    if is_permutation(A):
        print(*A)
    else:
        print(-1)
