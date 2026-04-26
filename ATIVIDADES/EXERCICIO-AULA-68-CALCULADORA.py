
"""
@author: Robson Costa
@date: 26/04/2026

Calculadora ultilizando um While
"""


while True:
    
    numero1  = input('Digite o primeiro número: ')
    numero2  = input('Digite o Segundo  número: ')    
    operador = input('Digite o operador [+] [-] [*] [/] : ')
    numeros_validos = None
    operador_permitidos = '+ - * /'
    operadores_validos = None
    numero1_float = 0
    numero2_float = 0
    try: #validação dos números se são válidos
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
        
    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print('Digite um valor válido.')
            continue
    
    
    if operador in operador_permitidos:
        operadores_validos = True
    else:
        operadores_validos = None
        print('Informe um operador valido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    if numeros_validos and operadores_validos:
        if operador == '+':
            print(f'A soma dos números {numero1_float} {operador} {numero2_float} = {numero1_float + numero2_float} ')
         
        elif operador == '-':
            print(f'A soma dos números {numero1_float} {operador} {numero2_float} = {numero1_float - numero2_float} ')
            
        elif operador == '*':
            print(f'A soma dos números {numero1_float} {operador} {numero2_float} = {numero1_float * numero2_float} ')
        
        else:
            if numero1_float == 0 or numero2_float == 0:
                print('Não é possível fazer divisão por zero')
            else:
                print(f'A soma dos números {numero1_float} {operador} {numero2_float} = {numero1_float / numero2_float} ')
                
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    
