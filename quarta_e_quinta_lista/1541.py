import math

while True:
    dados = list(map(int, input().split()))
    if len(dados) == 1 and dados[0] == 0:
        break
    if dados[2] == 0:
        dados[2] = 1

    area_referencia = dados[0] * dados[1]
    area_necessaria = area_referencia * 100 / dados[2]
    lado_necessario = int(math.sqrt(area_necessaria))
    print(lado_necessario)
