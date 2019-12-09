

frase = input()

len(frase.lower())

a = frase.lower().count('a')
e = frase.lower().count('e')
i = frase.lower().count('i')
o = frase.lower().count('o')
u = frase.lower().count('u')
espaco = frase.count(' ')

vogais = a + e + i + o + u

consoantes = len(frase) - vogais - espaco

print(frase)

print (f'Contagem de Vogais: {vogais}')

print(f'Contagem de Consoantes: {consoantes}')



