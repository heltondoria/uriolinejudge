CONDICAO_DE_SAIDA = 0

numero_lido = -1
while numero_lido != CONDICAO_DE_SAIDA:
    numero_lido = int(input())
    lista_numeros = [numero for numero in range(1, numero_lido + 1)]
    indice = 0
    numeros_descartados = list()
    texto_cartas_descartadas = 'Discarded cards:'
    while indice < len(lista_numeros) - 1:
        numero_descartado = lista_numeros[0]
        numeros_descartados.append(numero_descartado)
        numero_movido = lista_numeros[1]
        lista_numeros.remove(lista_numeros[0])
        lista_numeros.remove(lista_numeros[0])
        lista_numeros.append(numero_movido)
        if texto_cartas_descartadas == 'Discarded cards:':
            texto_cartas_descartadas = texto_cartas_descartadas + ' ' + str(numero_descartado)
        else:
            texto_cartas_descartadas = texto_cartas_descartadas + ', ' + str(numero_descartado)
    if len(lista_numeros) > 0:
        print(texto_cartas_descartadas.strip())
        print('Remaining card: {}'.format(lista_numeros[0]))