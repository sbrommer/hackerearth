def readints():
    return list(map(int, input().split()))

T = int(input())

for _ in range(T):
    balloons = readints()
    n = int(input())

    solves = list(map(sum, zip(*[readints() for _ in range(n)])))

    print(max(balloons) * min(solves) + min(balloons) * max(solves))
