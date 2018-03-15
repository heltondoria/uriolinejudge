cardapio = {1001: 1.50,
            1002: 2.50,
            1003: 3.50,
            1004: 4.50,
            1005: 5.50}

quantidade_produtos = int(input())
total = 0.0
for i in range(quantidade_produtos):
    compra = list(map(int, input().split()))
    total = total + (compra[1] * cardapio[compra[0]])
print("{:.2f}".format(total))
