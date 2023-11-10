def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def gcd(a, b, d=0):
    if a == b:
        return a * 2 ** d
    if even(a) and even(b):
        return gcd(a // 2, b // 2, d + 1)
    if even(a):
        return gcd(a // 2, b, d)
    if even(b):
        return gcd(a, b // 2, d)
    
    a, b = max(a, b), min(a, b)
    return gcd(b, a - b, d)


def even(n):
    return not n % 2


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    m = lcm(a, b)
    print(m // a, m // b)
