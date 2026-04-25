from datetime import date

# Declaração de dvariáveis
nome = 'Robson'
sobrenome = 'Costa'
idade = 32
ano_nascimento = date.today().year - idade
maior_idade = idade >= 18
altura_metros = 1.80

print('Nome', nome)
print('Sobrenome', sobrenome)
print('Idade', idade)
print('Ano de nascimento', ano_nascimento)
print('É maior de idade', maior_idade)
print('Altura em metros', altura_metros)
