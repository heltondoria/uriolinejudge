quantidade_casos = int(input())
for i in range(quantidade_casos):
    candidato = input().split()
    if candidato[0] == "Thor":
        print("Y")
    else:
        print("N")
