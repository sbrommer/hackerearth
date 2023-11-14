T = int(input())

for i in range(T):
    x, k = map(int, input().split())

    for p in range(60,-1,-1):
        if k ** p <= x:
            x -= k ** p

    print('YES' if not x else 'NO')
