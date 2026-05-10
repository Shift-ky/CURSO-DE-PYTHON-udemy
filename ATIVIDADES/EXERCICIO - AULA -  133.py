"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
 
lista = [1, 2, 3, 4, 5, 6]
numeros = set()
primeiro_duplicado = None
duplicado = False

for i in lista:
    duplicado = i in numeros
    if duplicado and primeiro_duplicado is None:
        primeiro_duplicado = i
    else:
        primeiro_duplicado = -1
    numeros.add(i)
    
    

print(f'primeiro duplicado é {primeiro_duplicado}')
    

