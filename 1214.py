quantidade_cases = int(input())
for i in range(quantidade_cases):
    valores = input().split()
    quantidade_alunos = int(valores[0])
    notas = list(map(int, valores[1::]))
    total_notas = sum(notas[0::])
    media = total_notas / quantidade_alunos
    alunos_acima_media = 0
    for nota in notas:
        if nota > media:
            alunos_acima_media += 1
    percentual_acima_media = (alunos_acima_media * 100.000)/ quantidade_alunos

    print("{:.3f}%".format(percentual_acima_media))
