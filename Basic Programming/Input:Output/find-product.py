from itertools import accumulate


def last(iterable):
    *_, last = iterable
    return last


input()
A = map(int, input().split())

print(int(last(accumulate(A, lambda a, b: a * b % (1e9 + 7)))))
