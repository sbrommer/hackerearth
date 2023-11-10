NM, *board = [[int(cell) for cell in line.split()]
              for line in open(0).readlines()]

N, M = NM

row_attack = [sum(row) for row in board]
col_attack = [sum(col) for col in zip(*board)]

max_attack = 0
x, y = 0, 0

for i in range(N):
    for j in range(M):
        attack = row_attack[i] + col_attack[j] - 2 * board[i][j]

        if attack > max_attack:
            max_attack = attack
            x, y = i, j

print(x + 1, y + 1)
