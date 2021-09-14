print('\033[0:30:41mTeste\033[m')
print('\033[4:33:44mTeste\033[m')
print('\033[1:35:43mTeste\033[m')
print('\033[30:42mTeste\033[m')
print('\033[7:30mTeste\033[m')


nome = 'Guanabara'
cores = {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'pretoebranco':'\033[7;30m'}

print('Olá, Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
