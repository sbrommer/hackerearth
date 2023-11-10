from math import sqrt


def triangular(n):
    return int(n * (n + 1) // 2)


# find the largest triangular number smaller than n
def largest_triangular(n):
    k = int((1 + sqrt(8 * n + 1)) // 2 - 1)
    return k, triangular(k)


# parse input
N = int(input())
A = list(map(int, input().split()))

# get triangular info (t = last number added to get T, T = triangular number)
t, T = largest_triangular(len(A))

# initialize sum and maximum for rolling window
s = sum(A[:T])
m = s

# roll the window
for i in range(1, N):
    # if the window gets too big,
    # update window and get new sum of window
    if i + T > N:
        T -= t
        t -= 1
        s = sum(A[i:i + T])

    # else update sum of window
    else:
        s -= A[i - 1]
        s += A[i + T - 1]

    # update max sum
    m = max(m, s)

print(m)
