S = input()

for s in S:
    print(s.upper() if s.islower() else s.lower(), end='')
