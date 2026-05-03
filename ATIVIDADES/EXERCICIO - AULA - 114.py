'''
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
'''


def soma(*numeros):
    valor = 1
    numeros = list(*numeros)
    for i in numeros:
        valor *= int(i)
    return valor

numeros = []
entrada = 0 

while True:
    
    entrada = input('Digite um valor: ')
    
    if entrada.isdecimal():
        numeros.append(entrada)
    else:
        entrada = None
        print('Digite apenas números')
        break
    
    
    
    saida = input('Quer adicionar outro número [S]im / [N]ão: ').lower().startswith('n')
    
    
    if saida is True:
        break
if entrada is not None:
    saida_dados = soma(numeros)
    print(f'A multiplicação dos números é {saida_dados}')


    