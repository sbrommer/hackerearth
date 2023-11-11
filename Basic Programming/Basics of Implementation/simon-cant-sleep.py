h, m = map(int, input().split(':'))

print(h + (12 * m >= 60 * (h % 12) + m ) - (h >= 12))
