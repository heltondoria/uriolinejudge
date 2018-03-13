while True:
    try:
        numero_lesmas = input()
        lesmas = list(map(int, input().split()))
        lesma_mais_rapida = max(lesmas)
        if lesma_mais_rapida >= 20:
            print(3)
        elif 10 < lesma_mais_rapida < 20:
            print(2)
        else:
            print(1)
    except:
        break