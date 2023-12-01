import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    computador = random.choice(opcoes)

    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if escolha_jogador in opcoes:
        print(f"Computador escolheu {computador}")
        print(f"Voce escolheu {escolha_jogador}")

        if escolha_jogador == computador:
            print ("Empate")
        elif (
            (escolha_jogador == 'pedra' and computador == 'tesoura') or
            (escolha_jogador == 'pepel' and computador == 'pedra') or
            (escolha_jogador == 'tesoura' and computador == 'pepel')
        ):
            print("Voce ganhou!")
        else:
            print("Voce perdeu!")
    else:
        print("Escolha invalida. por favor, escolha entre pedra, papel ou tesoura")

jogar()