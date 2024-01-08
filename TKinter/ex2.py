import tkinter as tk
from tkinter import ttk
import requests
import json

class Container:
   def __init__(self, parent):
       self.myParent = parent
       self.container = tk.Frame(parent)
       self.container.pack()

       self.titulo = ttk.Label(self.container, text="Consultar API por CEP")
       self.titulo.config(font=("Arial", 14, "normal", "normal"))

       self.uf_label = ttk.Label(self.container, text="UF (2 caracteres):")
       self.uf_label.config(font=("Arial", 12, "normal", "normal"))
       self.uf_entry = ttk.Entry(self.container)
       self.uf_entry.config(font=("Arial", 12, "bold", "bold"))

       self.municipio_label = ttk.Label(self.container, text="Município:")
       self.municipio_label.config(font=("Arial", 12, "normal", "normal"))
       self.municipio_entry = ttk.Entry(self.container)
       self.municipio_entry.config(font=("Arial", 12, "bold", "bold"))

       self.logradouro_label = ttk.Label(self.container, text="Logradouro:")
       self.logradouro_label.config(font=("Arial", 12, "normal", "normal"))
       self.logradouro_entry = ttk.Entry(self.container)
       self.logradouro_entry.config(font=("Arial", 12, "bold", "bold"))

       self.consultar_button = tk.Button(self.container, text="Consultar", command=self.consultar)
       self.consultar_button.configure(font=("Verdana", 16, "normal", "normal"), foreground="blue")

       self.resultado_label = ttk.Label(self.container, text="")
       self.resultado_label.config(font=("Comic Sans ms", 16, "normal", "normal"), foreground="green")

       self.titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
       self.uf_label.grid(row=1, column=0, padx=10, pady=10)
       self.uf_entry.grid(row=1, column=1, padx=10, pady=10)
       self.municipio_label.grid(row=2, column=0, padx=10, pady=10)
       self.municipio_entry.grid(row=2, column=1, padx=10, pady=10)
       self.logradouro_label.grid(row=3, column=0, padx=10, pady=10)
       self.logradouro_entry.grid(row=3, column=1, padx=10, pady=10)
       self.consultar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
       self.resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

   def consultar(self):
       uf = self.uf_entry.get()
       municipio = self.municipio_entry.get()
       logradouro = self.logradouro_entry.get()
       retorno = ""
       response = requests.get('https://viacep.com.br/ws/'+uf+'/'+municipio+'/'+logradouro+'/json/')
       resultado = json.loads(response.text)
       if isinstance(resultado, list):
           if resultado:
               retorno = "Endereços encontrados:\n"
               for endereco in resultado:
                   retorno += f'''
CEP: {endereco['cep']}
Logradouro: {endereco['logradouro']}
Complemento: {endereco['complemento']}
Bairro: {endereco['bairro']}
Localidade: {endereco['localidade']}
UF: {endereco['uf']}
DDD: {endereco['ddd']}
'''
           else:
               retorno = "Nenhum endereço encontrado."
       else:
           retorno = "Erro na consulta da API."

       self.resultado_label.config(text=retorno)


def main():
   raiz = tk.Tk()
   raiz.title("Consulta CEP, UF, Municipio e Logradouro.")
   apl = Container(raiz)
   raiz.mainloop()


if __name__ == "__main__":
   main()
