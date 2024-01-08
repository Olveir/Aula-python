n1 = float(input("insira a primeira nota: "))
if n1 < 0 or n1 > 10:
    print("Invalido")
    n1=0
n2 = float(input("insira a segunda nota: "))
if n2 < 0 or n2 > 10:
    print("Invalido")
    n2=0
n3 = float(input("insira a terceira nota: "))
if n3 < 0 or n3 > 10:
    print("Invalido")
    n3= 0
soma = (n1*1) + (n2*1.5) + (n3*2)
media = soma/4.5
print("A sua média foi de: {:.2f}".format(media))
if media == 0:
    print("SR")
elif media > 0 and media < 2:
    print("II")
elif media >= 2 and media < 5:
    print("MI")
elif media >= 5 and media < 7:
    print("MM")
elif media >= 7 and media < 9:
    print("MS")
else:
    print("SS.")
