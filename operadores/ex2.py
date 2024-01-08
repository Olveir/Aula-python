peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc= peso/(altura**2)
print("O seu imc é: {:.2f}".format(imc))
