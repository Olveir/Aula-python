# Descriptografia:

frase = input("Digite uma frase:")
frase2= ""
fraseEmb=""
fraseDes=""
for i in range(0, len(frase), 1):
    codif = ord(frase[i]) - 1
    frase2 += chr(codif)
print(frase2)


if len(frase2) % 2 == 1:
    max = int(len(frase2)*2) + 1
else:
    max = int(len(frase2)*2)


for j in range(0, len(frase2), 1):
    if j %2== 0:
        fraseEmb += frase2[j]


for k in range(0, len(frase2), 1):
    if k %2 ==1:
        fraseDes += frase2[k]


fraseEmb += fraseDes[::-1]

print(fraseEmb)