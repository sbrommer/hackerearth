def sum_of_digits(n):
    return sum(map(int, list(str(n))))


def special(n):
    return not sum_of_digits(n) % 4


T = int(input())

for _ in range(T):
    a = int(input())
    while not special(a):
        a += 1
    print(a)
