n = int(input())
villages = input()
houses = villages.split('.')

if max(map(len, houses)) > 1:
    print('NO')
else:
    print('YES')
    print(villages.replace('.', 'B'))
