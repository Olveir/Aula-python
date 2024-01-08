import sqlite3


def main():
   # Criar uma conexão com o banco de dados
   cnn = sqlite3.connect("produto.db")

   # Criar um cursor para a conexão
   c = cnn.cursor()

   # Template de comando SQL de inserção
   cmd = "INSERT INTO tb_prod(nme_prod, vlr_prod, qtd_prod) VALUES (?, ?, ?)"


   while True:
       print(">>> Inclusão de Produto")
       nome  = input("Nome: ")
       valor  = float(input("Valor: "))
       qtd = int(input("Quantidade: "))

       # Gravando dados na tabela
       c.execute(cmd, [nome, valor, qtd])
       cnn.commit()
       print("-> Produto incluído com sucesso")
       opc = input("Sair S/N? ")
       if opc == 'S':
           break

   # Fechar a conexão com o banco de dados
   c.close()
   cnn.close()


if __name__ == "__main__":
   main()
