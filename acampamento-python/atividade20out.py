totalCompra=float(input("Insira o valor total da compra: "))
totalCompra=float(input("Insira o valor total da compra: "))
notasCinquenta=int(input("Insira a quantidade de notas de R$50 entregue pelo cliente: "))
notasDez=int(input("Insira a quantidade de notas de R$10 entregue pelo cliente: "))
notasCinco=int(input("Insira a quantidade de notas de R$5 entregue pelo cliente: "))
totalPagamento=float((notasCinquenta*50)+(notasDez*10)+(notasCinco*5))
troco=float(totalPagamento-totalCompra)
print("O total da sua compra foi de R$",round(totalCompra, 2))
print("Você nos forneceu:")
print(notasCinquenta,"notas de R$50.")
print(notasDez,"notas de R$10.")
print(notasCinco,"notas de R$5.")
print("Totalizando R$",round(totalPagamento, 2))
print("Seu troco é de R$",round(troco, 2))