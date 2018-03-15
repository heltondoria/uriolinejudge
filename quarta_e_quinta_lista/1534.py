while True:
    try:
        dimensao_matriz = int(input())
    except:
        break

    linha = ''
    for i in range(dimensao_matriz):
        for j in range(dimensao_matriz):
            if j == dimensao_matriz - 1 - i:
                elemento = 2
            elif i == j:
                elemento = 1
            else:
                elemento = 3
            linha = "{}{}".format(linha, elemento)
        print(linha)
        linha = ''
