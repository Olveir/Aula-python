n1 = float(input("insira a primeira nota: "))
if n1 < 0 or n1 > 10:
    print("Invalido")
n2 = float(input("insira a segunda nota: "))
if n2 < 0 or n2 > 10:
    print("Invalido")
n3 = float(input("insira a terceira nota: "))
if n3 < 0 or n3 > 10:
    print("Invalido")
soma = n1 + n2 + n3
media = soma/3
print("A sua média foi de: {:.2f}".format(media))
if media>= 5:
    print("Você foi aprovado.")
else:
    print("Você reprovou.")
