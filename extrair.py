# extrair.py
# coding: utf-8

import os
import zipfile
import sys

def main(path):
    if not os.path.exists(path):
        print('Arquivo {} não existe'.format(path))
        sys.exit(-1)
    elif not str(path).endswith('.zip'):
        print(f'Arquivo {path} não é .zip')
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print('Arquivos Extraídos')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Por Favor, coloque o nome de um arquivo .zip')
    else:
        main(sys.argv[1])