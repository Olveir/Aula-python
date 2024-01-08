import sqlite3

def main():
   # Criar uma conexão com o banco de dados
   cnn = sqlite3.connect("produto.db")

   # Criar um cursor para a conexão
   c = cnn.cursor()

   # Template de comando SQL de consulta
   cmd_sel = "SELECT * FROM tb_prod WHERE idt_prod = ?"
   cmd_del = "DELETE FROM tb_prod WHERE idt_prod=?"

   while True:
       print(">>> Exclusão de produtos")
       id = int(input("Qual o identificador do produto? "))

       # Consultando dados na tabela
       c.execute(cmd_sel, [id])
       dados = c.fetchone()
       if dados is None:
           print("ID não encontrado")
           continue

       print("Dados atuais:", dados)
       conf = input("Confirma exclusão S/N? ")
       if conf == 'S':
           # Excluindo dados na tabela
           c.execute(cmd_del, [id])
           cnn.commit()
           print("Produto Excluído!")

       opc = input("Sair S/N? ")
       if opc == 'S':
           break

   # Fechar a conexão com o banco de dados
   c.close()
   cnn.close()

if __name__ == "__main__":
   main()
