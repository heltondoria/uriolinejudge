quantidade_cases = int(input())
for i in range(quantidade_cases):
    valores = input().split()
    quantidade_alunos = int(valores[0])
    notas = [int(valor) for valor in valores if valor != valores[0]]
    total_notas = 0
    for nota in notas:
        total_notas = total_notas + nota
    media = total_notas / quantidade_alunos

    notas_acima_media = 0
    alunos_acima_media = 0
    for nota in notas:
        if int(nota) > media:
            alunos_acima_media = alunos_acima_media + 1
    percentual_acima_media = alunos_acima_media / quantidade_alunos

    print("{:3.3f}%".format(percentual_acima_media *100))