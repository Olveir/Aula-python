import sqlite3


def main():
   # Criar uma conexão com o banco de dados
   cnn = sqlite3.connect("produto.db")

   # Criar um cursor para a conexão
   c = cnn.cursor()

   # Criar a tabela de produtos
   c.execute("""
   CREATE TABLE tb_prod (
     idt_prod INTEGER PRIMARY KEY AUTOINCREMENT,
     nme_prod VARCHAR(30) NOT NULL,
     vlr_prod DECIMAL(8,2) NOT NULL,
     qtd_prod INT NOT NULL
   );
   """)

   # Fechar a conexão com o banco de dados
   c.close()
   cnn.close()

   print("Tabela de Produtos criada")


if __name__ == "__main__":
   main()
