"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

 Author Robson Paiva
"""

       
cpf = input('Digite o seu CPF: ').strip().replace('.','').replace('-','')

if len(cpf) != 11:
    cpf = None

try:
    
    cpf_nove_digitos = cpf[0:9] 
    multiplicador_nove_digitos = int(10)
    multiplicador_nove_digitos_soma = 0
    nove_digitos_multiplicado_por_dez = 0
    resto_divissão_nove_digitos = 0
    digito_validador_1 = 0
    
    #Laço de repetição para fazer o calculo do primeiro dígito
    for i in cpf_nove_digitos:
    
        multiplicador_nove_digitos_soma += (int(i)*multiplicador_nove_digitos)
        multiplicador_nove_digitos -= 1
    
    #Calculos e validações do primeiro dígito
    nove_digitos_multiplicado_por_dez = multiplicador_nove_digitos * 10
    resto_divissão_nove_digitos = nove_digitos_multiplicado_por_dez % 11
    digito_validador_1 = resto_divissão_nove_digitos if resto_divissão_nove_digitos < 9 else 0 

    
    
    multiplicador_dez_digitos = 11
    dez_digito_multiplicado = 0
    dez_digito_mutiplicado_dez = 0 

    cpf_dez_digitos = cpf[:9] + str(digito_validador_1)

    for j in cpf_dez_digitos:
        dez_digito_multiplicado += int(j) * multiplicador_dez_digitos
        multiplicador_dez_digitos -= 1
    
    dez_digito_mutiplicado_dez = dez_digito_multiplicado * 10

    resto_divisao_dez_digito = dez_digito_mutiplicado_dez % 11
    digito_validador_2 = resto_divisao_dez_digito if resto_divisao_dez_digito < 9 else 0


    if cpf[9] == str(digito_validador_1) and cpf[10] == str(digito_validador_2):
        print('CPF VÁLIDO') 
    else:
        print('CPF INVÁLIDO')
except IndexError:
    print('CPF Invormado está faltando informações, informar um CPF válido')
except TypeError:
    print('CPF com quantidade incorreta de caracteres')
except ValueError:
    print('CPF com letras informado, por gentileza inform os 11 dígitos do seu CPF')