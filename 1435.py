def print_matriz(matrix, size):
    width = 3

    for x in range(size):
        for i, num in enumerate(matrix[x]):
            if i == size - 1:
                print('{0:{width}}'.format(num, width=width), end='')
            else:
                print('{0:{width}}'.format(num, width=width), end=' ')
        print()
    print('')


while True:
    tamanho = int(input())
    if tamanho == 0:
        break

    matriz = [[1 for i in range(tamanho)] for j in range(tamanho)]
    linha = " "
    for indice_linha in range(len(matriz)):
        for indice_coluna in range(len(matriz[indice_linha])):
            x = min(indice_linha + 1, tamanho - indice_linha)
            y = min(indice_coluna + 1, tamanho - indice_coluna)
            matriz[indice_linha][indice_coluna] = min(x, y)

    print_matriz(matriz, tamanho)
