def verifica_quantidade_parenteses(expressao):
    parenteses_abertura = list()
    parenteses_fechamento = list()

    for caracter in expressao:
        if caracter == ")":
            if len(parenteses_abertura) == 0:
                parenteses_fechamento.append(caracter)
                break
            else:
                parenteses_abertura.pop()
        elif caracter == "(":
            parenteses_abertura.append(caracter)

    if len(parenteses_abertura) == len(parenteses_fechamento):
        esta_balanceado = True
    else:
        esta_balanceado = False

    return "correct" if esta_balanceado else "incorrect"

if __name__ == '__main__':
    try:
        while True:
            expressao = input()

            if not expressao:
                break
            print(verifica_quantidade_parenteses(expressao))

    except EOFError:
        pass
