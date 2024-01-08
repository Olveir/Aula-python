# Criptografia:

frase = input("Digite uma frase: ")
frase2= ""
fraseEmb=""


for i in range(0, len(frase), 1):
    codif = ord(frase[i]) + 1
    frase2 += chr(codif)
print("A frase cifrada é:", frase2)


if len(frase2) % 2 == 1:
    max = int(len(frase)/2) + 1
else:
    max = int(len(frase)/2)


for j in range(0, max, 1):
    fraseEmb += frase2[0+ j] + frase2[-1 -j]


if len(frase2)%2 ==0:
    print(frase)
else:
    print(fraseEmb[0:len(frase2)])
