import os.path

def registra():
    if (os.path.isfile('c:\\aula0906\\nomes.txt')):
        arq = open('c:\\aula0906\\nomes.txt', 'r')
        dados = arq.readlines()
        existe = True
        arq.close()
    else:
        existe = False

    arq = open('c:\\aula0906\\nomes.txt', 'w')
    nome = input('Qual o nome para registro? ')
    if existe:
        arq.writelines(dados)
    arq.write(nome + '\n')
    arq.close()

def lista():
    arq = open('c:\\aula0906\\nomes.txt', 'r')
    for nome in arq:
        print(nome, end='')
    arq.close()

def html():
    parte1 = '''
    <!DOCTYPE html>
    <html lang="pt-br">


    <head>
        <meta charset="windows-1251">
        <title>Tabela</title>
        <style>
            th,
            td {
                border: 2px solid blue;
                background-color: #eeeeff;
            }
        </style>
    </head>


    <body>
        <h1 style="text-align: center;">Tabela com Nomes</h1>
        <hr />
        <br />


        <table style="width:100%; margin:auto; border-collapse: collapse;">
            <tr>
                <th>Número</th>
                <th>Nome</th>
            </tr>
    '''

    parte_dinamica = ''

    parte3 = '''
        </table>


    </body>


    </html>

    '''

    arq = open('c:\\aula0906\\nomes.txt', 'r')
    num = 1
    for nome in arq:
        parte_dinamica += '''
        <tr>
                <td>{}</td>
                <td>{}</td>
            </tr>

        '''.format(num, nome)
        num += 1
    arq.close()

    arqTxt = open('c:\\aula0906\\tabela.html', 'w')
    arqTxt.writelines(parte1 + parte_dinamica + parte3)
    arqTxt.close()
    print('Fim de escrita do arquivo')

sair = False
while not sair:
    print('\n' * 2)
    print('1 - Registrar nome')
    print('2 - Listar nomes')
    print('3 - Gerar HTML')
    print('4 - Sair')
    opc = int(input('Qual a opção? '))
    if opc == 1: registra()
    elif opc == 2: lista()
    elif opc == 3: html()
    elif opc == 4: sair = True
