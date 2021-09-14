s = float(input('Qual o salário atual? '))
if s >= 1000.00:
    a = ((s*0.1)+s)
else:a = ((s*0.15)+s)
print('O salário será {:.2f}'.format(a))
