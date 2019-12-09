salario = int(input('Digite seu salário: '))
imposto = float(input('Digite seu imposto em % (ex: 27.5): '))

print(f'Valor real: {salario - (salario * (imposto / 100))}')
