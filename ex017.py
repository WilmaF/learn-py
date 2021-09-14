from math import sqrt
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
h = sqrt((co**2)+(ca**2))
print('A hipotenusa vai medir {:.2f}'.format(h))
