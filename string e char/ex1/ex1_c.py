#Terceiro Padrão

frase = input("Digite uma palavra ou sequência de caracteres: ")
n = len(frase)
resultado = [None] * n

for i in range(n // 2):
   resultado[i * 2] = frase[n - i - 1]
   resultado[i * 2 + 1] = frase[i]

if n % 2 == 1:
   resultado[n - 1] = frase[n // 2]

strInv = ''.join(resultado)
print("Resultado: {}".format(strInv))
