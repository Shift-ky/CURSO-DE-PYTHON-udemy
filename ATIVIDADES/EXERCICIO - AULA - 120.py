

def duplica(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

numero = 2

duplicar = duplica(2)
triplicar = duplica(3)
quadruplicar = duplica(4)


print(f'{duplicar(2)} {triplicar(3)} {quadruplicar(4)}')
