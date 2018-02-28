um_quilo_em_trigo = 12000
quantidade_cases = int(input())
for i in range(quantidade_cases):
    quantidade_casas = int(input())
    quantidade_trigo = 1

    for casa  in range(1, quantidade_casas):
        quantidade_trigo = quantidade_trigo + pow(2,casa)

    peso_trigo = quantidade_trigo // um_quilo_em_trigo
    print("{} kg".format(peso_trigo))

