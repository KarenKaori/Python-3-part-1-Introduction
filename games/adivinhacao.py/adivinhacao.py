print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
allowed_attempts = 3
rodada = 1

while rodada <= allowed_attempts:
    print(f"Tentativa {rodada} de {allowed_attempts}")
    #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    # print("Type: ", type(chute))
    # input sempre retorna uma string no python3

    chute = int(chute_str)
    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if menor:
            print("Você errou, o seu chute foi menor que o numero secreto.")
        elif maior:
            print("Você errou, o seu chute foi maior que o numero secreto.")
        rodada = rodada + 1

print("Fim do jogo")
