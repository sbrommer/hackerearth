def even(n):
    return not n % 2


def valid_digits(tag):
    ix = [[0, 1], [3, 4], [4, 5], [7, 8]]
    return all(even(int(tag[i]) + int(tag[j])) for i, j in ix)


def valid_letter(tag):
    return tag[2] not in 'AEIOUY'


def valid(tag):
    return valid_digits(tag) and valid_letter(tag)


print('valid' if valid(input()) else 'invalid')
