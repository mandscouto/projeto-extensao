from random import randint
jogos = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jog1 = input('Jogada: ')
jog2 = input('Jogada: ')
if (jog1.lower == 'x' || jog2.lower == 'x'):
    print('Jogo encerrado.') 