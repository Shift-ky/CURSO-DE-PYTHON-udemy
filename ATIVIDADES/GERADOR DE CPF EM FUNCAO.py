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

       
cpf = '746824890'
    
    #Variáveis do primeiro dígito
cpf_nove_digitos = cpf[0:9] 
multiplicador_nove_digitos = 10
multiplicador_nove_digitos_soma = 0
nove_digitos_multiplicado_por_dez = 0
resto_divissão_nove_digitos = 0
digito_validador_1 = 0
    
    #Laço de repetição para fazer o calculo do primeiro dígito
for i in cpf_nove_digitos:
    
    multiplicador_nove_digitos_soma += (int(i)*multiplicador_nove_digitos)
    multiplicador_nove_digitos -= 1
    
    #Calculos e validações do primeiro dígito
nove_digitos_multiplicado_por_dez = multiplicador_nove_digitos_soma * 10
resto_divissão_nove_digitos = nove_digitos_multiplicado_por_dez % 11
digito_validador_1 = resto_divissão_nove_digitos if resto_divissão_nove_digitos < 9 else 0 

print(multiplicador_nove_digitos_soma)
print(nove_digitos_multiplicado_por_dez)
print(digito_validador_1)