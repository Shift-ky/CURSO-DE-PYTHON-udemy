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
"""

       
cpf = input('Digite o seu CPF: ').strip().replace('.','').replace('-','')


cpf_validacao = cpf[0:8] 
multiplicador  = int(10)
multiplicacao_numeros = 0
multiplicacao_numeros_por_10 = 0
resto_divissão = 0
validador_digito_1 = 0

for i in cpf_validacao:
    
    multiplicacao_numeros += (int(i)*multiplicador)
    multiplicador -= 1
    
multiplicacao_numeros_por_10 = multiplicacao_numeros * 10
resto_divissão = multiplicacao_numeros_por_10 % 11
validador_digito_1 = resto_divissão if resto_divissão < 9 else 0 
print(multiplicacao_numeros)
print (multiplicacao_numeros_por_10)
print(validador_digito_1)

if cpf[9] == str(validador_digito_1):
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')