'''

FAÇA UMA LISTA DE COMPRAR COM LISTAS O USUÁRIO DEVE TER A POSSIBILIDADE DE
INSERIR, APAGAR E LISTAR VALORES DA SUA LISTA NÃO PERMITA QUE O PROGRAMA QUEBRA
COM ERROS DE INDICE INEXISTENTES NA LISTA.
'''
lista_compra = []
validacao_das_opcoes = '123'
while True:
    
    opcao = input('[1] listar [2] adicionar [3] apagar ')
    
    if opcao not in validacao_das_opcoes:
        print('Digite 1, 2 ou 3 para fazer alguma ação')
        continue
    
    if opcao == '1':
        if len(lista_compra) == 0:
            print('Lista de compras vazia, adicione produtos')
        
        index = 0
        for i in lista_compra:
            print(f'{index} {i}')
            index += 1
            
    elif opcao == '2':
        
        adicionar = input('Informe o produto que deseja adicionar ')
        lista_compra.append(adicionar)
        print(f'{adicionar} adicionado com sucesso')
        
    elif opcao == '3':
        try:
            exclusao = input('Digite o numero do item que deseja excluir: ')
            
            if exclusao.isdecimal():
                exclusao = int(exclusao)
            else:
                print('Informe um valor numérico para fazer a exclusão do item')   
                continue
            lista_compra.pop(exclusao)
            print(f'Produto excluído com sucesso')
        except:
            print('Indice não existente na lista. Por favor informar um correto')
        
    else:
        print('O códico nunca era para chegar aqui')
        
