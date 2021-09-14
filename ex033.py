a = int(input('Escreve o primeiro número '))
b = int(input('Escreva o segundo número '))
c = int(input('Escreva o terceiro número '))
if a>b  and a>c:
    print('O maior número é {}'.format(a))
elif b>a  and b>c:
    print('O maior número é {}'.format(b))
elif c > b and c > a:
        print('O maior número é {}'.format(c))
if a<b  and a<c:
    print('O menor número é {}'.format(a))
elif b<a  and b<c:
    print('O menor número é {}'.format(b))
elif c < b and c < a:
        print('O menor número é {}'.format(c))