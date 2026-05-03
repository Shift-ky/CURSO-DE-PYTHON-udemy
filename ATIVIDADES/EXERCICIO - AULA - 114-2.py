

def validar(numero):
    valor = int(numero) % 2
    
    if valor == 0:
        return f'O {numero} é PAR'
    return f'{numero} é ÍMPAR'
    





entrada = input('Digite um valor para saber se é ímpa ou parr: ')
saida = validar(entrada)
print(saida)