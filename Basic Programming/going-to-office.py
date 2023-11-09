D = int(input())
Oc, Of, Od = map(int, input().split())
Cs, Cb, Cm, Cd = map(int, input().split())

O = Oc + Od * max(D - Of, 0)
C = Cb + Cm * (D // Cs) + Cd * D

print('Online Taxi' if O <= C else 'Classic Taxi')
