from prettytable import PrettyTable
import requests
import json

dolar = 0
iene = 0
euro = 0
peso = 0
dolarC = 0
ieneC = 0
euroC = 0
pesoC = 0
def consultar_moeda(real):
   response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,JPY-BRL,ARS-BRL/')
   cotacao = json.loads(response.text)
   if cotacao.get("erro"):
       print("Erro")
   else:
       saida = PrettyTable(["Campo", "Valor", "Conversão"])

       dolar = float(cotacao['USDBRL']['high'])
       dolarC = (round(float(real/dolar)*100)/100)
       saida.add_row(["DOLAR:", dolar, dolarC])

       peso = float(cotacao['ARSBRL']['high'])
       pesoC = (round(float(real / peso)*100)/100)
       saida.add_row(["PESO ARGENTINO:", peso, pesoC])

       euro = float(cotacao['EURBRL']['high'])
       euroC = (round(float(real / euro)*100)/100)
       saida.add_row(["EURO:", euro, euroC])

       iene = float(cotacao['JPYBRL']['high'])
       ieneC = (round(float(real / iene)*100)/100)
       saida.add_row(["IENE JAPONES:", iene, ieneC])

       print(saida)


def main():
   while True:
       print()
       print("-" * 30)
       print("Quantos reais você tem? ([-1]-para terminar):")
       real = float(input())
       if real == -1:
           break
       consultar_moeda(real)


if __name__ == "__main__":
    main()
