import tkinter as tk
import tkinter.messagebox
from musicas import Musica, MusicaDAO


class Container:
  def __init__(self, parent):
      self.myParent = parent
      self.container = tk.Frame(parent)
      self.container.pack()

      self.titulo = tk.Label(self.container, text="Música")
      self.titulo.config(font=("Arial", 20, "bold", "bold"), foreground="blue")

      self.lb_idt = tk.Label(self.container, text="Identificador:")
      self.lb_idt.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_idt = tk.Entry(self.container)
      self.et_idt.config(font=("Arial", 12, "bold", "bold"), width=5)
      self.bt_idt = tk.Button(self.container, text="Consultar", command=self.consultar)
      self.bt_idt.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

      self.lb_nome = tk.Label(self.container, text="Nome da Música:")
      self.lb_nome.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_nome = tk.Entry(self.container)
      self.et_nome.config(font=("Arial", 12, "bold", "bold"), width=30)

      self.lb_artista = tk.Label(self.container, text="Nome do Artista:")
      self.lb_artista.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.et_artista = tk.Entry(self.container)
      self.et_artista.config(font=("Arial", 12, "bold", "bold"), width=30)

      self.lb_texto_us = tk.Label(self.container, text="Letra Inglês:")
      self.lb_texto_us.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.tx_texto_us = tk.Text(self.container, height=5, width=40)
      self.tx_texto_us.config(font=("Arial", 12, "bold", "bold"))

      self.lb_texto_br = tk.Label(self.container, text="Letra Português:")
      self.lb_texto_br.config(font=("Arial", 12, "normal", "normal"), foreground="green")
      self.tx_texto_br = tk.Text(self.container, height=5, width=40)
      self.tx_texto_br.config(font=("Arial", 12, "bold", "bold"))

      self.bt_novo = tk.Button(self.container, text="Novo", command=self.novo)
      self.bt_novo.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
      self.bt_salvar = tk.Button(self.container, text="Salvar", command=self.salvar)
      self.bt_salvar.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")
      self.bt_excluir = tk.Button(self.container, text="Excluir", command=self.excluir)
      self.bt_excluir.configure(font=("Arial", 14, "normal", "normal"), foreground="blue")

      self.titulo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

      self.lb_idt.grid(row=1, column=0, padx=10, pady=10, sticky="e")
      self.et_idt.grid(row=1, column=1, padx=10, pady=10, sticky="w")
      self.bt_idt.grid(row=1, column=2, padx=10, pady=10, sticky="w")

      self.lb_nome.grid(row=2, column=0, padx=10, pady=10, sticky="e")
      self.et_nome.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.lb_artista.grid(row=3, column=0, padx=10, pady=10, sticky="e")
      self.et_artista.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.lb_texto_us.grid(row=4, column=0, padx=10, pady=10, sticky="e")
      self.tx_texto_us.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.lb_texto_br.grid(row=5, column=0, padx=10, pady=10, sticky="e")
      self.tx_texto_br.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="w")

      self.bt_novo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
      self.bt_salvar.grid(row=6, column=1, padx=10, pady=10, sticky="w")
      self.bt_excluir.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="w")

      self.dao = MusicaDAO()

  def consultar(self):
      idt = self.et_idt.get()
      if idt.isdigit() and idt != "0":
         idt_int = int(idt)
         m = self.dao.consultar(idt_int)
         if m.idt == 0:
            tkinter.messagebox.showwarning("Não encontrado", "ID não encontrado na base de dados")
            self.et_idt.focus()
         else:
            self.limpar()
            self.et_idt.insert(0, str(m.idt))
            self.et_nome.insert(0, m.nome)
            self.et_artista.insert(0, m.artista)
            self.tx_texto_us.delete("1.0", tk.END)
            self.tx_texto_br.delete("1.0", tk.END)
            self.tx_texto_us.insert("1.0", m.texto_us)
            self.tx_texto_br.insert("1.0", m.texto_br)
            self.et_nome.focus()
      else:
         tkinter.messagebox.showerror("Inválido", "Valor inválido para consulta por ID")
         self.et_idt.focus()

  def limpar(self):
     for entry in (self.et_idt, self.et_nome, self.et_artista):
        entry.delete(0, tk.END)

     self.tx_texto_us.delete("1.0", tk.END)
     self.tx_texto_br.delete("1.0", tk.END)

  def novo(self):
         self.limpar()
         self.et_idt.insert(0, "0")
         self.et_nome.focus()

  def vazio(self):
         if self.et_nome.get() == "":
            tkinter.messagebox.showerror("Nome Obrigatório", "Insira o nome da música")
            self.et_nome.focus()
            return True

         if self.et_artista.get() == "":
            tkinter.messagebox.showerror("Nome do artista invalido", "Insira um artista válido")
            self.et_artista.focus()
            return True

         if self.tx_texto_us.get("1.0", tk.END) == "":
            tkinter.messagebox.showerror("Letra em inglês inválida", "Insira letras válidas")
            self.tx_texto_us.focus()
            return True

         if self.tx_texto_br.get("1.0", tk.END) == "":
            tkinter.messagebox.showerror("Letra em portugês inválida", "Insira letras válidas")
            self.tx_texto_br.focus()
            return True

         return False

  def salvar(self):
         if self.vazio():
            return

         if not self.et_idt.get().isdigit() or int(self.et_idt.get()) == 0:
            m = Musica(nome=self.et_nome.get(), artista=self.et_artista.get(), texto_br=self.tx_texto_br.get("1.0", tk.END),
                      texto_us=self.tx_texto_us.get("1.0", tk.END))
            self.dao.incluir(m)
            self.novo()
            tkinter.messagebox.showinfo("Inclusão", "Inclusão efetuada com sucesso")
            self.et_nome.focus()
         else:
            idt = self.et_idt.get()
            if idt.isdigit():
               idt_int = int(idt)
               m = Musica(idt=idt_int, nome=self.et_nome.get(), artista=self.et_artista.get(), texto_br=self.tx_texto_br.get("1.0", tk.END),
                          texto_us=self.tx_texto_us.get("1.0", tk.END))
               self.dao.alterar(m)
               tkinter.messagebox.showinfo("Alteração", "Alteração efetuada com sucesso")
               self.et_nome.focus()
            else:
               tkinter.messagebox.showerror("Inválido", "Valor inválido no ID")
               self.et_idt.focus()

  def excluir(self):
         idt = self.et_idt.get()
         if idt.isdigit() and idt != "0":
            idt_int = int(idt)
            self.dao.excluir(idt_int)
            tkinter.messagebox.showinfo("Exclusão", "Exclusão efetuada com sucesso")
            self.novo()
         else:
            tkinter.messagebox.showerror("Inválido", "Valor inválido para exclusão por ID")
            self.et_idt.focus()


def main():
   raiz = tk.Tk()
   raiz.title("Cadastro de Produtos")
   apl = Container(raiz)
   raiz.mainloop()


if __name__ == "__main__":
   main()
