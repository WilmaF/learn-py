n = input(str('Qual é o seu nome? ')).strip()
separa = n.split()
q = len(separa)-1
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é: {} '.format(separa[q]))
