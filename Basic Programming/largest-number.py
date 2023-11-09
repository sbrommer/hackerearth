N, K = input().split()
K = int(K)

M = ''

while 0 < K < len(N):
    # find the subarray from which we
    # can choose the largest element
    n = N[:K + 1]

    # find the largest element
    i = n.index(max(n))

    # add this to the answer
    M += n[i]

    # remove this element and the
    # previous i elements from N
    N = N[i + 1:]
    # we have K - i elements still to remove
    K -= i

# The answer is M plus anything left
# in N that shouldn't be removed.
print(M + ('' if K else N))
