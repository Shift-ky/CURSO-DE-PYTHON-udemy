"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("\033c", end="")
hora = input('Digite uma hora fechada: ')

try:
    hora = int(hora)
    hora_valida = hora >=  0 and hora <= 24
    bom_dia     = hora >=  0 and hora <= 11 
    boa_tarde   = hora >= 12 and hora <= 17    
    if hora_valida:
        if bom_dia:
            print('Bom dia!')
        elif boa_tarde:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Informe um valor de 0 á 24, para ser uma hora válida')
except:
    print('Digite um número válido')