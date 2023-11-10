import numpy as np


def readints():
    return map(int, input().split())


t = int(input())

for _ in range(t):
    N, _ = readints()
    As = sorted(list(readints()))

    lunches = [A > N for A in np.cumsum(As)] + [True]

    print(lunches.index(True))
