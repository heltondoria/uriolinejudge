import timeit

CONDICAO_DE_SAIDA = 0

def le_cartas():
    cartas_lidas = list()
    try:
        while True:
            carta = int(input())
            if carta == CONDICAO_DE_SAIDA:
                break
            cartas_lidas.append(carta)
            cartas_descartadas, carta_restante = remove_cartas(cartas_lidas.copy())
            imprime_resultado(cartas_descartadas, carta_restante)
    except EOFError:
        pass

def remove_cartas(cartas_lidas):
    cartas_descartadas = list()
    if len(cartas_lidas) >= 2:
        while len(cartas_lidas) > 1:
            cartas_descartadas.append(cartas_lidas.pop(0))
            cartas_lidas.append(cartas_lidas.pop(0))

    return cartas_descartadas, cartas_lidas.pop()


def imprime_resultado(cartas_descartadas, carta_restante):

    texto_cartas_descartadas = 'Discarded cards: {}'.format(', '.join(map(str, cartas_descartadas)))

    print(texto_cartas_descartadas.strip())
    print('Remaining card: {}'.format(carta_restante))


if __name__ == '__main__':
    le_cartas()
