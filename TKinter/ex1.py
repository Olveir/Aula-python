from tkinter import *


class Container:
   def __init__(self, parent):
       self.myParent = parent
       self.container = Frame(parent)
       self.container.pack()

       self.primeiro_numero_label = Label(self.container, text="Digite o primeiro número:")
       self.primeiro_numero_label.config(font=("Arial", 14, "normal", "normal"))
       self.primeiro_numero_entry = Entry(self.container)
       self.primeiro_numero_entry.config(font=("Arial", 14, "bold", "bold"))

       self.segundo_numero_label = Label(self.container, text="Digite o segundo número:")
       self.segundo_numero_label.config(font=("Arial", 14, "normal", "normal"))
       self.segundo_numero_entry = Entry(self.container)
       self.segundo_numero_entry.config(font=("Arial", 14, "bold", "bold"))

       self.somar_button = Button(self.container, text="Somar", command=lambda:self.realiza_operacao("soma"))
       self.subtrair_button = Button(self.container, text="Subtrair", command=lambda:self.realiza_operacao("subtracao"))
       self.multiplicar_button = Button(self.container, text="Multiplicar",command=lambda:self.realiza_operacao("multiplicacao"))
       self.dividir_button = Button(self.container, text="Dividir", command=lambda:self.realiza_operacao("divisao"))

       self.somar_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")
       self.subtrair_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")
       self.multiplicar_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")
       self.dividir_button.config(font=("Verdana", 16, "normal", "normal"), foreground="blue")

       self.resultado_label = Label(self.container, text="")
       self.resultado_label.config(font=("Comic Sans ms", 16, "normal", "normal"), foreground="green")

       self.primeiro_numero_label.grid(row=0, column=0, padx=10, pady=10)
       self.primeiro_numero_entry.grid(row=0, column=1, padx=10, pady=10)

       self.segundo_numero_label.grid(row=1, column=0, padx=10, pady=10)
       self.segundo_numero_entry.grid(row=1, column=1, padx=10, pady=10)

       self.somar_button.grid(row=2, column=0, padx=10, pady=10)
       self.subtrair_button.grid(row=2, column=1, padx=10, pady=10)
       self.multiplicar_button.grid(row=3, column=0, padx=10, pady=10)
       self.dividir_button.grid(row=3, column=1, padx=10, pady=10)

       self.resultado_label.grid(row=4, columnspan=2, padx=10, pady=10)

   def realiza_operacao(self, operacao):
       primeiro_numero = int(self.primeiro_numero_entry.get())
       segundo_numero = int(self.segundo_numero_entry.get())
       if primeiro_numero and segundo_numero:
           primeiro_numero = int(primeiro_numero)
           segundo_numero = int(segundo_numero)
           resultado = None

           if operacao == "soma":
               resultado = primeiro_numero + segundo_numero
           elif operacao == "subtracao":
               resultado = primeiro_numero - segundo_numero
           elif operacao == "multiplicacao":
               resultado = primeiro_numero * segundo_numero
           elif operacao == "divisao":
               if segundo_numero != 0:
                   resultado = primeiro_numero / segundo_numero
               else:
                   resultado = "Erro: Divisão por zero"

           self.resultado_label.config(text=f"O Resultado da operação é: {resultado}")
       else:
           self.resultado_label.config(text="Digite ambos os números")



def main():
   raiz = Tk()
   raiz.title("Calculadora de de operações aritméticas")
   apl = Container(raiz)
   raiz.mainloop()

if __name__ == "__main__":
   main()
