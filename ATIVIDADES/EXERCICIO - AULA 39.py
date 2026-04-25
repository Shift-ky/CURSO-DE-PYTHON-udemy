"""
@author: Robson Costa
@since: 2020-09-14
@version: 1.0


Exercicio - Aula 39 - Faça um programa que compare dois e mostre o maior e o menor valor.
"""

try: 
   num1 = int(input("Digite o primeiro número: "))
   num2 = int(input("Digite o primeiro número: "))
   
except ValueError:
    print("Valor inválido. Por favor, digite um número inteiro.")

if num1 == num2:
    print(f"Os dois valores são iguais Primeiro valor digitado ({num1}) segundo valor digitado ({num2})")
elif num1 > num2:
    print(f" O número ({num1}) é maior do que o segundo digitado ({num2})")
else:
    print(f"O número ({num2}) é maior do que o primeiro digitado ({num1})")