# salario_real.py
salario = int(input('Digite seu salário: '))
imposto = input('Digite seu imposto em % (ex: 27.5): ')

imposto = float(imposto) if imposto else 27.5

#if  imposto == '':
#    imposto = 27.5
#else:
#    imposto = float(imposto)

print(f'Valor real: {salario - (salario * (imposto / 100))}')
