"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)


  
cpf = '74682489070'#input('Digite o seu CPF: ').strip().replace('.','').replace('-','')
cpf = cpf if len(cpf) == 11 else None
multiplicador_dez_digitos = 11
dez_digito_multiplicado = 1

cpf_dez_digitos = cpf[:9] + '7'

for j in cpf_dez_digitos:
    dez_digito_multiplicado += int(j) * multiplicador_dez_digitos
    multiplicador_dez_digitos -= 1
print(cpf_dez_digitos)
print(dez_digito_multiplicado)