linhas = int(input('Digite a quantidade de linhas da piramide: ')) + 1

for i in range(1, linhas):
   print(' ' * (linhas - i), '#'  * i, ' ', '#' * i, sep = "")
   
