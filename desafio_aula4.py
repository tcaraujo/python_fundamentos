
def tirar_vogais(frase):
    vogais = 'aeiouAEIOU'
    frase_nova = ''
    for letra in frase:
        if letra not in vogais:
            frase_nova = frase_nova + letra
    return frase_nova


frase = input('Digite sua frase: ')
resultado = tirar_vogais(frase)
print(resultado)
