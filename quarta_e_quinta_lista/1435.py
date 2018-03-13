def get_identity_square_matrix(size):
    matrix = [[1 for column_index in range(size)] for row_index in range(size)]
    return matrix


while True:
    tamanho = int(input())
    if tamanho == 0:
        break

    matriz = get_identity_square_matrix(tamanho)
    linha = " "
    for indice_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz[indice_linha])):
            x = min(indice_linha + 1, tamanho - indice_linha)
            y = min(indice_coluna + 1, tamanho - indice_coluna)
            matriz[indice_linha][indice_coluna] = min(x, y)
            elemento = "{}  ".format(str(matriz[indice_linha][indice_coluna]))
            linha = "{} {}".format(linha, elemento)
        linha = "{}{}".format(linha.rstrip(), '\n ')
    print("{}".format(linha.rstrip(' ')))
