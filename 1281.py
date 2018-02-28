quantidade_cases = int(input())
for i in range(quantidade_cases):
    total_compras = 0
    quantidade_produtos = int(input())
    produtos_feira = dict()
    for case in range(quantidade_produtos):
        produto, preco = input().split()
        produtos_feira[produto] = float(preco)

    quantidade_compras = int(input())
    lista_compras = dict()
    for compra in range(quantidade_compras):
        produto, quantidade = input().split()
        lista_compras[produto] = int(quantidade)

    for item in lista_compras.keys():
        total_compras = total_compras + (lista_compras[item] * produtos_feira[item])

    print("R$ {:.2f}".format(total_compras))