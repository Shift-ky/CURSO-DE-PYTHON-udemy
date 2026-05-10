#def ordenar(item):
#    return item['nome']

def exibir(lista):
    for item in lista:
        print(item)
    print('\n')

lista = lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]

#lista.sort(key=ordenar)
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])


print(exibir(l1))
print(exibir(l2))
