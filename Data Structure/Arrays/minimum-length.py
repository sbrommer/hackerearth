from operator import eq

def readints():
    return list(map(int, input().split()))

T = int(input())

for _ in range(T):
    N = int(input())
    A = readints()
    B = readints()

    equal = [eq(*z) for z in zip(A, B)]
    print(N - equal[::-1].index(False) - equal.index(False), )
