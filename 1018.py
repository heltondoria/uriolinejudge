def calcula_qtd_notas(initial_amount):
    current_amount = initial_amount
    money = (100, 50, 20, 10, 5, 2, 1)
    i = 0
    print(current_amount)
    while(i < len(money)):
        notas, current_amount = divmod(current_amount, money[i])
        print("{} nota(s) de R$ {},00".format(notas, money[i]))
        i = i + 1

if __name__ == '__main__':
    entrada = int(input())
    calcula_qtd_notas(entrada)