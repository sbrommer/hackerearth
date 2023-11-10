T = int(input())
 
for _ in range(T):
    input()
    monsters = map(int, input().split())
    alive = []
 
    for m in monsters:
        while alive and alive[-1] <= m:
            alive.pop()
        alive.append(m)
        print(len(alive), end=' ')
    print()
