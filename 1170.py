quantidade_cases = int(input())
for i in range(quantidade_cases):
    quantidade_comida = float(input())

    duracao_da_comida_em_dias = 0
    while quantidade_comida > 1:
        quantidade_comida = quantidade_comida / 2
        duracao_da_comida_em_dias = duracao_da_comida_em_dias + 1

    print("{} dias".format(duracao_da_comida_em_dias))