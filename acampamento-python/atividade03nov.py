n1 = int(input("nsira a nota alcançada na primeira avaliação: "))
n2 = int(input("nsira a nota alcançada na segunda avaliação: "))
n3 = int(input("nsira a nota alcançada na terceira avaliação: "))
media = (n1+n2+n3)/3
if(media<70):
    print("Sua média é {0:.1f}".format(media)," e você está reprovado.")
else:
    print("Sua média é {0:.1f}".format(media)," e você está aprovado.")