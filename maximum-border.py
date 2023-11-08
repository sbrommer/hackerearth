def get_table():
    n = int(input().split()[0])

    return [input() for _ in range(n)]


def border(table):
    return max(map(border_row, table))


def border_row(row):
    return max(map(len, row.split('.')))


def transpose(table):
    return map(''.join, zip(*table))


t = int(input())

for _ in range(t):
    table = get_table()

    print(max(border(table), border(transpose(table))))
