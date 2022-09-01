def CaluladoraDeFatorial():
    # Recebendo o número para calcular seu fatorial:
    numero = (int(input("Digite o número no qual você deseja saber o fatorial: ")))
    # Criando o nosso fatorial que irá retornar nosso valor final:
    fatorial = 1
    # Criando o nosso loop while, para decrementar nosso número até que ele chegue em 1 (fatorial de 5 = 5*4*3*2*1).
    while numero >= 1:
        fatorial *= numero  # fatorial = fatorial * numero
        numero -= 1
    # Retornando o resultado do fatorial:
    return print(fatorial)

CaluladoraDeFatorial()