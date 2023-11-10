matchsticks = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
               '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

T = int(input())

for _ in range(T):
    # get number of matchsticks
    N = input()
    m = sum(matchsticks[n] for n in N)

    # print largest possible number
    digits = m // 2
    print('7' if m % 2 else '1', end='')
    print(''.join(['1'] * (m // 2 - 1)))
