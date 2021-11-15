from random import randint
jogos = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções: 
[r] Pedra
[p] Papel
[r] Tesoura''')
jog1 = input('Jogada: ')
jog2 = input('Jogada: ')
while (jog1.lower() != 'x' or jog2.lower() != 'x'):
    if(jog1 != 'r' or jog1 != 'p' or jog1 != 't' or jog2 != 'r' or jog2 != 'p' or jog2 != 't'):
        print('Essa jogada é inválida. Tente novamente.')
    elif(jog1 == jog2):
        print('Deu empate! Vamos de novo...')
jog1 = input('Jogada: ')
jog2 = input('Jogada: ')