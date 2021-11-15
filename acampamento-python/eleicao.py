candidatoA = 0
candidatoB = 0
candidatoC = 0  
voto = 0
nulos = 0
while (voto >= 0):
    voto = int(input('Digite o número do candidato 1, 2 ou 3 : '))
    if (voto == 1):
        candidatoA = candidatoA + 1
    elif (voto == 2): 
        candidatoB = candidatoB + 1
    elif (voto == 3):
        candidatoC = candidatoC + 1
    else:
        nulos = nulos + 1

print('Eleição finalizada. O resultado é: ')
print('Candidato 1: ',candidatoA,' votos.')
print('Candidato 2: ',candidatoB,' votos.')
print('Candidato 3: ',candidatoC,' votos.')
print('Votos nulos: ',nulos,' votos.')
