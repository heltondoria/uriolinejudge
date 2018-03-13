tomadas_utilizadas_entre_reguas = 3
tomadas_por_regua = list(map(int, input().split()))
print(sum(tomadas_por_regua) - tomadas_utilizadas_entre_reguas)
