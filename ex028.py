import random

n = [0,1,2,3,4,5]
e = int(input('digite um número entre 0 e 5: '))
r = random.choice(n)
print('O numero era {}'.format(r))
if e == r:
    print('Você acertou!')
else:
    print('Tente novamente.')
