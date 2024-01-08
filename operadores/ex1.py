compra = float(input("Insira o valor da compra: "))
desconto = int(input("Insira o valor do desconto de 0 a 100: "))

desconto = compra/100 * desconto
preFin = compra - desconto
print("Valor sem desconto: R${}\nDesconto: R${}\nValor final: R${}".format(compra,desconto,preFin))
