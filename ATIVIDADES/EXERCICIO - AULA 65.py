



nome = 'Robson Paiva'
nome_com_asterisco = ' '
contador = 0

quantidade_letra_nome = len(nome)

while quantidade_letra_nome > contador:
    print(contador)
    nome_com_asterisco += nome[int(contador)]
    nome_com_asterisco += '*'
    contador +=1
    
print(nome_com_asterisco)