import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

# Usando for ___ in range (start, stop, step):
numero_secreto = random.randrange(1,101)
#print(numero_secreto)

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Nível: "))

if nivel == 1:
    allowed_attempts = 15
elif nivel == 2:
    allowed_attempts = 10
else:
    allowed_attempts = 5

points = 1000

for rodada in range(1, allowed_attempts + 1):
    print(f"Tentativa {rodada} de {allowed_attempts}")
    #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    # print("Type: ", type(chute))
    # input sempre retorna uma string no python3

    chute = int(chute_str)
    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if chute <= 0 or chute > 100:
        print("Você deve digitar um numero entre 1 e 100!")
        continue

    if acertou:
        print("Você acertou e fez {} pontos!".format(points))
        break
    else:
        if menor:
            print("Você errou, o seu chute foi menor que o numero secreto.")
            if (rodada == allowed_attempts):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, points))
        elif maior:
            print("Você errou, o seu chute foi maior que o numero secreto.")
            if (rodada == allowed_attempts):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, points))
        rodada = rodada + 1
        lost_points = abs(numero_secreto - chute)
        points = points - lost_points



print("Fim do jogo")

##############################################################################################
# Usando while
#
# numero_secreto = 42
# allowed_attempts = 3
# rodada = 1
#
# while rodada <= allowed_attempts:
#     print(f"Tentativa {rodada} de {allowed_attempts}")
#     #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#     chute_str = input("Digite o seu número: ")
#     print("Você digitou: ", chute_str)
#     # print("Type: ", type(chute))
#     # input sempre retorna uma string no python3
#
#     chute = int(chute_str)
#     acertou = chute == numero_secreto
#     menor = chute < numero_secreto
#     maior = chute > numero_secreto
#
#     if acertou:
#         print("Você acertou!")
#         break
#     else:
#         if menor:
#             print("Você errou, o seu chute foi menor que o numero secreto.")
#         elif maior:
#             print("Você errou, o seu chute foi maior que o numero secreto.")
#         rodada = rodada + 1
#
# print("Fim do jogo")
##############################################################################################