"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Declaração de dados
palavra_secreta = 'aranha'
letra_digitada = ' '
letras_digitadas = ' '
palavra = ''
validar_letra_entrada = None
tentativas = 0 

## Fim da declaração de dados

while True:
    
    letra_digitada =  input('Digite uma letra: ')
    letras_digitadas += letra_digitada
    validar_letra_entrada = None
    tentativas += 1
    
    
    # Validação para ser digitado apenas letras
    if letra_digitada.isalpha():
        validar_letra_entrada = True
    else:
        validar_letra_entrada = None
        
    if validar_letra_entrada is None:
        print('Digite uma letra ou a palavra completa')
        print(palavra)
        
        continue
    
    palavra= ''
    
    for i in palavra_secreta:
        if i in letras_digitadas:
            palavra += i
        else:
            palavra += '*'
    
    print(palavra)
    
    if palavra_secreta == palavra:
        
        print(f'Parabéns você acertou a palavra após {tentativas} tentativas')
        break
    
        
            
    
    
    
    