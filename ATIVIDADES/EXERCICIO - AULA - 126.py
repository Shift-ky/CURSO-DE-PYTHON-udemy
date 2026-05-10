
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 50/2? ',
        'Opções': ['24', '25', '22', '11'],
        'Resposta': '25',
    },
]
contador = 0
contador_acertos = 0
resposta_validador = False
while True:
    count = 0
    print(perguntas[contador]['Pergunta'])
    print()
    print('Opções:')

    for i in perguntas[contador]['Opções']:
        print(f'{count}) {i}')
        count += 1
    print()
    resposta = input('Escolha a opção: ')
    
    try:
    
        resposta_validador = resposta.isdecimal()
        if resposta_validador is False:
            print('Errou ❌')
 
        validar = perguntas[contador]['Opções'][int(resposta)] == perguntas[contador]['Resposta']

        if validar:
            print('Acertou 👍\n')
            contador_acertos += 1
        else:
            print('Errou ❌\n')
    except:
       ...        
    contador += 1
    if contador == len(perguntas):
        break
print(f'Você acertou {contador_acertos}\n de {len(perguntas)} perguntas')