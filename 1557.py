def print_matriz(matrix, size):
    width = len(str(matrix[size - 1][size - 1]))

    for x in range(size):
        for i, num in enumerate(matrix[x]):
            if i == size - 1:
                print('{0:{width}}'.format(num, width=width), end='')
            else:
                print('{0:{width}}'.format(num, width=width), end=' ')
        print()
    print('')


while True:
    n = int(input())
    if n == 0:
        break

    potencia = 0
    linha = " "
    matriz = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j] = 2 ** potencia
            potencia += 1
        potencia = i + 1

    print_matriz(matriz, n)
