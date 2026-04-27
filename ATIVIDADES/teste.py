palavra_secreta = 'mercha'
letras_ja_digitadas = ''

print('Adivinhe a palavra secreta')

while True:
    letra_digitada = input('Digite uma letra: ')
    letras_ja_digitadas += letra_digitada

    palavra_formada = ''
    
    for letra in palavra_secreta:
        if letra in letras_ja_digitadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Você ganhou!')
        break