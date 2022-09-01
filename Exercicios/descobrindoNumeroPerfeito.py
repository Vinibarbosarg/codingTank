def VerificaPerfeito():
    divisores = []
    n = int(input("Digite um número: "))
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    soma_divisores = sum(divisores)
    print(f'Os divisores são: {divisores}')
    if soma_divisores == n:
        return print("True")
    else:
        return print('False')


VerificaPerfeito()
