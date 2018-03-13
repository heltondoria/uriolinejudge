frase = "LIFE IS NOT A PROBLEM TO BE SOLVED"

quantidade_letras = int(input())
texto = ""
for i in range(quantidade_letras):
    texto = "{}{}".format(texto, frase[i])
print(texto)
