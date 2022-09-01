numero_teste = (int(input("Digite um número inteiro para descobrir se ele é primo: ")))
# Contador para contagem da quantidade de multiplos do número.
contador = 0
# Utilzando o for para criar e percorrer uma lista do 2 até o número digitado
quantidade_de_divisiveis = 0
# Criando uma lista para armazenar os divisores.
lista_divisores = []

for valor in range(2, numero_teste):
    # Se o número dividido pelo valor da lista tiver resto 0, saberemos que o número pode ser dividido por esse valor, dessa forma ele não pode ser primo e adicionamos +1 a nossa varíavel de contagem de divisiveis.
    if numero_teste % valor == 0:
        lista_divisores.append(valor)
        quantidade_de_divisiveis += 1

    # Caso a quantidade de divisores seja igual a 0, saberemos que ele é divisivel apenas por 1 ele mesmo, haja vista que ambos não fizeram parte do nosso range no for.
if not quantidade_de_divisiveis == 0:
    print(f'{numero_teste} é divisivel por: {lista_divisores}, portanto não é primo!')

else:
    print("É um número primo!")
    print(f"{numero_teste} é divisível apenas por 1 e por ele mesmo!")


