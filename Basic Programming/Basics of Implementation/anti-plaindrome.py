T = int(input())

for _ in range(T):
    S = input()
    print(-1 if len(set(S)) == 1 else ''.join(sorted(list(S))))
