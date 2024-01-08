import sqlite3
from prettytable import PrettyTable


def main():
    # Criar uma conexão com o banco de dados
    cnn = sqlite3.connect("produto.db")

    # Criar um cursor para a conexão
    c = cnn.cursor()

    # Template de comando SQL de consulta
    cmd = "SELECT * FROM tb_prod WHERE nme_prod LIKE '%' || ? || '%'"

    while True:
        print(">>> Consulta de Produtos")
        parte = input("Digite parte do nome do produto: ")

        # Consultando dados na tabela
        c.execute(cmd, [parte])
        tab = PrettyTable(['Identificador', 'Nome', 'Valor', 'Quantidade'])

        for (id, nome, valor, qtd) in c.fetchall():
            tab.add_row([id, nome, valor, qtd])

        print(tab)
        opc = input("Sair S/N? ")
        if opc == 'S':
            break

    # Fechar a conexão com o banco de dados
    c.close()
    cnn.close()

if __name__ == "__main__":
    main()
