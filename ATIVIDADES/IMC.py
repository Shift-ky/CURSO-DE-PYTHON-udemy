"""
criar uma calculadora que mostre o IMC de uma pessoa
"""

nome = 'Robson'
altura = 1.80
peso = 80

imc = peso / (altura * altura)

print(f'{nome} tem {altura} ')
print(f'pesa {peso} e seu IMC é {imc:.2f}')