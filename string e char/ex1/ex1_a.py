#Primeiro Padrão

frase = str(input("Insira uma palavra: "))
saida = ''
for i, char in enumerate(frase):
        saida += char * (i + 1)
print(saida)
