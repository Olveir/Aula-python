import tkinter as tk
import tkinter.ttk as ttk
import pygame

from musicas import MusicaDAO

class Container:
   def __init__(self, parent):
       self.myParent = parent
       self.container = tk.Frame(parent)
       self.container.configure(background="#DDDDFF")
       self.container.pack()

       self.dao = MusicaDAO()

       self.titulo = tk.Label(self.container, text="Tocador de Músicas")
       self.titulo.config(font=("Arial", 20, "bold", "bold"), foreground="blue", background="#DDDDFF")

       self.lb_cb = tk.Label(self.container, text="Escolha a música:")
       self.lb_cb.config(font=("Arial", 12, "normal", "normal"), foreground="blue", background="#DDDDFF")
       musicas = self.dao.consultar_todos()
       nomes = []
       for musica in musicas:
           nomes.append(str(musica.idt) + "-" + musica.nome + "-" + musica.artista)
       self.cb_m = ttk.Combobox(self.container)
       self.cb_m["values"] = nomes
       self.cb_m.configure(state="readonly", width=40)
       self.cb_m.bind("<<ComboboxSelected>>", self.consultar)

       self.lb_m = tk.Label(self.container, text="")
       self.lb_m.config(font=("Arial", 14, "bold", "bold"), foreground="brown", background="#DDDDFF")

       self.lb_us = tk.Label(self.container, text="Música em Inglês")
       self.lb_us.config(font=("Arial", 14, "bold", "bold"), foreground="white", background="#DDDDFF")
       self.lb_br = tk.Label(self.container, text="Música em Português")
       self.lb_br.config(font=("Arial", 14, "bold", "bold"), foreground="white", background="#DDDDFF")
       self.lb_img = tk.Label(self.container, text="Imagem do artista/banda")
       self.lb_img.config(font=("Arial", 14, "bold", "bold"), foreground="white", background="#DDDDFF")

       self.tx_us = tk.Text(self.container)
       self.tx_us.configure(font=("Arial", 10, "bold", "bold"), foreground="gray", height=15, width=60)
       self.tx_us.justify = "left"
       self.tx_us.text = ""
       self.tx_br = tk.Text(self.container)
       self.tx_br.configure(font=("Arial", 10, "bold", "bold"), foreground="gray", height=15, width=60)
       self.tx_br.text = ""

       self.lb_imagem = tk.Label(self.container)
       self.lb_imagem.config(bg="#DDDDFF")

       self.titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

       self.lb_cb.grid(row=1, column=0, padx=10, pady=10, sticky="e")
       self.cb_m.grid(row=1, column=1, padx=10, pady=10, sticky="w")

       self.lb_m.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

       self.lb_us.grid(row=3, column=0, padx=10, pady=10)
       self.tx_us.grid(row=4, column=0, padx=10, pady=10)

       self.lb_img.grid(row=3, column=2, padx=10, pady=10)
       self.lb_imagem.grid(row=4, column=2, padx=10, pady=10)

       self.lb_br.grid(row=3, column=1, padx=10, pady=10)
       self.tx_br.grid(row=4, column=1, padx=10, pady=10)
       return

   def exibir_imagem(self, nome_artista):
       try:
           img_path = f"{nome_artista}.png"  # Supondo que o arquivo da imagem tenha o mesmo nome do artista/banda
           img = tk.PhotoImage(file=img_path)
           img = img.subsample(2)
           self.lb_imagem.config(image=img)
           self.lb_imagem.image = img  # Mantém uma referência à imagem para evitar a coleta de lixo
       except FileNotFoundError:
           print(f"Imagem para {nome_artista} não encontrada.")


   def consultar(self, event):
       self.limpar()
       dados = self.cb_m.get()
       lista = dados.split(sep="-")
       musica = self.dao.consultar(int(lista[0]))
       self.lb_m.config(text="Música: {} e Artista/Banda: {}".format(lista[1], lista[2]))

       num_linhas = musica.texto_us.count("\n")
       self.tx_us.configure(height=num_linhas)
       self.tx_br.configure(height=num_linhas)

       self.tx_us.insert("1.0", musica.texto_us)
       self.tx_br.insert("1.0", musica.texto_br)

       pygame.init()
       pygame.mixer.music.load(lista[1] + ".mp3")
       pygame.mixer.music.play()

       self.exibir_imagem(lista[2])

       return

   def limpar(self):
       self.lb_m.config(text="")
       self.tx_us.delete("1.0", "end")
       self.tx_br.delete("1.0", "end")
       return


def main():
   raiz = tk.Tk()
   raiz.title("PP-Player Python")
   apl = Container(raiz)
   raiz.mainloop()
   return


if __name__ == "__main__":
   main()

