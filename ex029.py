v = int(input('Qual a velocidade do carro?'))
if v <=80:
    print('Dirigindo bem.')
else:print('Você será multado em {:.2f}'.format((v-80)*7))
