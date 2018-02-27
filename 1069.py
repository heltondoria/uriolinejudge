def contar_diamantes(expressao):
    diamante_abertura = list()
    contador_diamantes = 0

    for caracter in expressao:
        if caracter == "<":
            diamante_abertura.append(caracter)
        elif caracter == ">" and len(diamante_abertura) > 0:
            diamante_abertura.pop()
            contador_diamantes = contador_diamantes + 1

    return contador_diamantes

if __name__ == '__main__':
    try:
        quantidade_cases = int(input())
        for case in range(quantidade_cases):
            expressao = input()
            print(contar_diamantes(expressao))

    except EOFError:
        pass
