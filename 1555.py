def funcao_rafael(x, y):
    return pow(3 * x, 2) + pow(y, 2)

def funcao_beto(x, y):
    return 2 * pow(x,2) + pow((5 * y),2)

def funcao_carlos(x, y):
    return  pow(y,3) - (100 * x)

quantidade_cases = int(input())
for i in range(quantidade_cases):
    nome_ganhador = ""
    x, y = input().split()
    rafael = funcao_rafael(int(x), int(y))
    beto = funcao_beto(int(x), int(y))
    carlos = funcao_carlos(int(x), int(y))

    if (beto > carlos and beto > rafael):
        nome_ganhador = 'Beto'
    elif (carlos > beto and carlos > rafael):
        nome_ganhador = 'Carlos'
    else:
        nome_ganhador = 'Rafael'

    print("{} ganhou".format(nome_ganhador))