from collections import Counter

zoo = input()
counter = Counter(zoo)

print('Yes' if counter['o'] == 2 * counter['z'] else 'No')
