
frase = 'a r a a a r a e e e r e e e r r r r r r r '

i = 0
quantidade_letra = 0
maior_letra_atual = 0
letra_atual = ' '
letra_maior_atual = ' '
quantidade_letra_maior = 0

while len(frase) > i:
    letra_atual = frase[i]
    quantidade_letra = frase.count(letra_atual)
    
    if frase[i] == ' ':
        i += 1
        continue
    
    if quantidade_letra > maior_letra_atual:
        letra_maior_atual = frase[i]
        quantidade_letra_maior = quantidade_letra
    

    i += 1
    
print(f'A letra "{letra_maior_atual}" apareceu {quantidade_letra_maior}x')