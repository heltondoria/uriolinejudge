alfabeto = "abcdefghijklmnopqrstuvwxyz"
quantidade_cases = int(input())
for i in range(quantidade_cases):
    frase = input().lower()
    contador = list()
    maior_ocorrencia = 0
    for letra in alfabeto:
        quantidade_letra = frase.count(letra)
        contador.append(quantidade_letra)
        if quantidade_letra > maior_ocorrencia:
            maior_ocorrencia = quantidade_letra

    resultado = ""
    for indice in range(len(contador)):
        if contador[indice] == maior_ocorrencia:
            resultado = resultado + alfabeto[indice]

    print("{}".format(resultado))