import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from cadAlunoView import AlunoView, AlunoQuery


class Container:
  def __init__(self, parent):
      self.myParent = parent
      self.container = tk.Frame(parent)
      self.container.pack()

      self.titulo = tk.Label(self.container, text="Consulta de Alunos")
      self.titulo.config(font=("Arial", 20, "bold", "bold"), foreground="blue")

      self.lb_nome = tk.Label(self.container, text="Nome do aluno ou parte:")
      self.lb_nome.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_nome = tk.Entry(self.container)
      self.et_nome.config(font=("Arial", 12, "bold", "bold"), width=40)

      self.lb_nota_min = tk.Label(self.container, text="Média mínima:")
      self.lb_nota_min.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_nota_min = tk.Entry(self.container)
      self.et_nota_min.config(font=("Arial", 12, "bold", "bold"), width=8)

      self.lb_nota_max = tk.Label(self.container, text="Média máxima:")
      self.lb_nota_max.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_nota_max = tk.Entry(self.container)
      self.et_nota_max.config(font=("Arial", 12, "bold", "bold"), width=8)

      self.bt_consultar = tk.Button(self.container, text="Buscar Dados", command=self.consultar)
      self.bt_consultar.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

      self.treeview = ttk.Treeview(self.container)
      self.treeview['show'] = 'headings'

      style = ttk.Style()
      style.theme_use('clam')
      style.configure("Treeview", font=("Arial", 12), foreground="blue")
      style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="blue", background="lightblue")

      self.treeview.configure(style="Treeview")

      self.treeview["columns"] = ("idt", "nme", "nota1", "nota2", "media", "mencao", "numero_faltas")

      self.treeview.heading("idt", text="Identificador")
      self.treeview.heading("nme", text="Nome do produto")
      self.treeview.heading("nota1", text="Primeira nota")
      self.treeview.heading("nota2", text="Segunda nota")
      self.treeview.heading("media", text="Média")
      self.treeview.heading("mencao", text="Menção")
      self.treeview.heading("numero_faltas", text="Número de faltas")

      self.titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

      self.lb_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
      self.et_nome.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.lb_nota_min.grid(row=2, column=0, padx=10, pady=10, sticky="e")
      self.et_nota_min.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.lb_nota_max.grid(row=3, column=0, padx=10, pady=10, sticky="e")
      self.et_nota_max.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.bt_consultar.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

      self.treeview.grid(row=5, column=0, columnspan=3)


  def excluir_linhas(self):
      for item in self.treeview.get_children():
          self.treeview.delete(item)

  def consultar(self):
       aq = AlunoQuery()
       nome = self.et_nome.get()
       nota_min = self.et_nota_min.get()
       nota_max = self.et_nota_max.get()

       nota_min = "0.0" if nota_min == "" else nota_min
       nota_max = "10.0" if nota_max == "" else nota_max

       try:
           float(nota_min)
           float(nota_max)
       except:
           tkinter.messagebox.showerror("Valores inválidos", "Algum valor é inválido")
           return

       self.excluir_linhas()

       lista = aq.view(nome, float(nota_min), float(nota_max))
       indice = 0
       for aluno in lista:
           self.treeview.insert(parent="", index=indice, values=(aluno.idt, aluno.nome, aluno.nota1,
                                                                 aluno.nota2, aluno.media, aluno.mencao, aluno.numero_faltas))
           indice += 1


def main():
  raiz = tk.Tk()
  raiz.title("Consulta de alunos")
  apl = Container(raiz)
  raiz.mainloop()

if __name__ == "__main__":
  main()
