n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
m = (n1 + n2)/2
if m >= 6.0:
    print('Aprovado')
else:
    print('Estude mais.')
print('A média é {:.1f}'.format(m))
print('Boas férias.')
