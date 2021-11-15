numero = int(input("Digite um número para ver sua tabuada: "))
for a in range (0, 11):
    print('{} x {:2} = {}'.format(numero,a,numero*a))