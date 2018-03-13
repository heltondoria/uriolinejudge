quantidade_casos = int(input())
for i in range(quantidade_casos):
    numero_termos = int(input())
    soma = 0
    for posicao_termo in range(numero_termos):
        if posicao_termo % 2 == 0:
            soma += 1
        else:
            soma -= 1
    print(soma)
