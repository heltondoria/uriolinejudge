quantidade_cases = int(input())
for i in range(quantidade_cases):
    strings = input().split()
    primeira_string = strings[0]
    segunda_string = strings[1]
    combinacao = ""

    maior_string = segunda_string
    if len(primeira_string) > len(segunda_string):
        maior_string = primeira_string

    for index in range(len(maior_string)):
        if len(primeira_string) > index:
            combinacao = combinacao + primeira_string[index]

        if len(segunda_string) > index:
            combinacao = combinacao + segunda_string[index]
    print("{}".format(combinacao))