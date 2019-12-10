# salario_real.py
salario = int(input('Digite seu salário: '))
imposto = 27.

while imposto > 0.:

    imposto = input('Digite seu imposto em % (ex: 27.5): ')
    if not imposto:
        imposto = 27
    else:
        imposto = float(imposto)
    
    print(f'Valor real: {salario - (salario * (imposto / 100))}')
    
