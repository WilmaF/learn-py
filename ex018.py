import math
a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O ângulo de {:.0f}º tem o SENO de {:.2f}  \n O ângulo de {:.0}º tem o COSSENO de {:.2f} \n O ângulo de {:.0f}º tem a TANGENTE DE {:.2f}'.format(a,sen,a,cos,a,tg))
