# Função para verificar os brinquedos em um parque que o usuário pode participar!

def AtracoesDisponiveisParaParticipacao():
    # Criando as variáveis para o usuário digitar:
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    altura = float(input("Digite a sua altura em centímetros: "))
    # Considerando o ano atual 2022 para descobrir a idade do usuário
    idade = 2022 - ano_nascimento
    # Criando lista com os brinquedos que o usuário poderá participar
    brinquedos_possiveis = []

    # If para avaliar se ele pode participar do carrossel: mais de 1 mertro de altura e pelo menos 3 anos de idade.
    if altura > 100 and idade >= 3:
        brinquedos_possiveis.append("Carrossel")
    # If para avaliar se ele pode participar da piscina de bolinhas: idade entre 4 e 9 anos, altura máxima de 1,30 m
    if 4 <= idade <= 9 and altura < 130:
        brinquedos_possiveis.append("Piscina de bolinhas")
    # If para avaliar se o usuário pode participar da Montanha-Russa: altura mínima de 1,10 m
    if altura >= 110:
        brinquedos_possiveis.append("Montanha-Russa")

    # Mostrando os brinquedos possíveis:
    print(f'Você pode participar dos seguintes brinquedos: {brinquedos_possiveis}')


AtracoesDisponiveisParaParticipacao()
