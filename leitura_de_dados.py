# leitura_de_dados.py
import os

def extract_name(name):
    return name.split('.')[0]

def read_lines(filename):
    _file = open(os.path.join('data/meta-data', filename), 'rt')
    data = _file.read().split('\n')
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split('\t')[:3]))
    return metadata

def prompt():
    print('\n0 que deseja ver?')
    print('(l) Listar entidades')
    print('(d) Exibir atributos de uma entidade')
    print('(r) Exibir referencias de uma entidade')
    print('(s) Sair do Programa')
    return input('')

def main():
    # dicionario nome entidade -> atributos
    meta = {}

    # dicionario identificador -> nome entidade
    keys = {}

    # dicionario relacionamentos
    relationships = {}

    for meta_data_file in os.listdir('data/meta-data'):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]

    opcao = prompt()
    while opcao != 's':
        if opcao == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif opcao == 'd':
            entity_name = input ('Nome da entidade: ')
            if not meta.get(entity_name, None):
                print('Entidade inexistente')
            else:  
                for col in meta[entity_name]:
                    print(col)
        elif opcao == 'r':
            entity_name = input('Nome da entidade: ')
            if not relationships.get(entity_name, None):
                print('Entidade inexistente')
            else:  
                other_entity = relationships[entity_name]
                print(other_entity)
        else:
            print('Inexistente\n')
        opcao = prompt()

if __name__ == '__main__':
    main()

