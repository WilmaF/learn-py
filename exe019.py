import random
a = str(input('Digite o nome do aluno: '))
b = str(input('Digite o nome do aluno: '))
c = str(input('Digite o nome do aluno: '))
d = str(input('Digite o nome do aluno: '))
escolhido = [a, b, c, d]
e = random.choice(escolhido)
print('O aluno escolhido foi {} '.format(e))
