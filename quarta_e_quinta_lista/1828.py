regras = {"tesoura": ["papel", "lagarto"],
          "papel": ["pedra", "Spock"],
          "pedra": ["lagarto", "tesoura"],
          "lagarto": ["Spock", "papel"],
          "Spock": ["tesoura", "pedra"]}


def resposta_sheldon(sheldon, raj):
    if sheldon == raj:
        frase = "De novo"
    elif regras[sheldon].count(raj):
        frase = "Bazinga"
    else:
        frase = "Raj trapaceou"
    return frase


quantidade_casos = int(input())
for i in range(quantidade_casos):
    sheldon, raj = input().split()
    print("Caso #{}: {}!".format(i+1, resposta_sheldon(sheldon, raj)))
