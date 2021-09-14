r1 = int(input('Escreva um dos lados '))
r2 = int(input('Escreva mais um lado '))
r3 = int(input('Escreva outro lado '))
h = r3
c = r1 + r2
if (r1 <= r2) and (r1 <= r3):
    h = r1
    c = r2 + r3
elif r2<= r1 and r2>= r3:
    h = r2
    c = r1 + r3
a = 'Não forma triângulo'
if r1<r2+r3 and r2< r1+r3 and r3<r1+r2:
    a = 'Forma Triangulo'
print(a)
