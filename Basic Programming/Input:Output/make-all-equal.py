from math import ceil
 
def get_steps(n, A, B):
    steps, m, i = 0, min(A), 0

    while i < n:
        # while we need to reduce Ai and we're allowed to, do so
        while A[i] > m and A[i] >= B[i]:
            A[i] -= B[i]
            steps += 1

        # if we need to reduce Ai, but we're not allowed to,
        # then it's not possible
        if A[i] > m and A[i] < B[i]:
            return -1

        # else we reduced Ai enough

        # if we have a new minimum, go back to the start of the array
        if A[i] < m:
            m = A[i]
            i = 0
        # else continue on the array
        else:
            i += 1

    return steps


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(get_steps(n, A, B))
