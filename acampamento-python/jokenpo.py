import random

jogadas = ["pedra", "papel", "tesoura"]

pontos_pc = 0
pontos_jog = 0

print("Pedra, papel e tesoura\n\n")
jog = ""

while jog.lower() != "x":
    jog = input("Qual a sua jogada?")
    if jog in jogadas:
        pc = random.choice(jogadas)
        print(f"Computador jogou: {pc}\n")

        # pedra ganha de tesoura
        if jog == "pedra" and pc == "tesoura":
            print("Você ganhou!")
            pontos_jog = pontos_jog + 1
        elif pc == "pedra" and jog == "tesoura":
            print("O computador ganhou!")
            pontos_pc = pontos_pc + 1
        
        # tesoura ganha de papel
        if jog == "tesoura" and pc == "papel":
            print("Você ganhou!")
            pontos_jog = pontos_jog + 1
        elif pc == "tesoura" and jog == "papel":
            print("O computador ganhou!")
            pontos_pc = pontos_pc + 1

        # papel ganha de pedra        
        if jog == "papel" and pc == "pedra":
            print("Você ganhou!")
            pontos_jog = pontos_jog + 1
        elif pc == "papel" and jog == "pedra":
            print("O computador ganhou!")
            pontos_pc = pontos_pc + 1

        print(f"\n\nVocê {pontos_jog} x {pontos_pc} Computador")
    elif jog.lower() != "x":
        print(f"Escolha uma das opções: {jogadas}")