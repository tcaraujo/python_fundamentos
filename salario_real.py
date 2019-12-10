# salario_real.py
salario = int(input('Digite seu salário: '))
imposto = input('Digite seu imposto em % (ex: 27.5): ')

#imposto = float(imposto) if imposto else 27.5

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)

if  imposto < 10:
    print('Baixo')
    
elif imposto >= 10. and imposto <=27:
    print('Médio')

elif imposto > 27. and imposto <= 100:
    print('Alto')

else:
    print('Imposto inválido')
    exit(1)
    #imposto = float(imposto)



print(f'Valor real: {salario - (salario * (imposto / 100))}')
