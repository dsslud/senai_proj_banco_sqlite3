import sqlite3

########################################################################
# CRIAÇÃO DO BANCO E TABELA:
def criar_tabela(cursor,):
    SQL_TABELA_Produtos = '''
        CREATE TABLE if NOT EXISTS produtos (
        ide INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER,
        preco TEXT
        )
    '''
    cursor.execute(SQL_TABELA_Produtos)

def cadastrar_produto(cursor):
    print("###### CADASTRO DE PRODUTO ######")
    nome = input("NOME: ")
    quantidade = input("QUANT.: ")
    preco = input("PRECO: ")

    SQL_INSERT = ''' 
        INSERT INTO produtos(nome, quantidade, preco) 
        VALUES (?, ?, ?)
    '''
    cursor.execute(SQL_INSERT, (nome, quantidade, preco))
    print(f" ###### PRODUTO {nome} CADASTRADO COM SUCESSO ######")

def estoque(cursor):
    print("###### PRODUTOS EM ESTOQUE ######")
    SQL_ESTOQUE = '''
        SELECT ide as "Codigo", nome as "Nome do produto", quantidade as "Quantidade em estoque", preco as "Preço"
        FROM produtos
    '''
    cursor.execute(SQL_ESTOQUE)
    produto = cursor.fetchall()
    print(produto)

def busca_produto(cursor):
    nome = input("###### BUSCA DE PRODUTO ######")
    SQL_BUSCA = '''
        SELECT ide, nome, quantidade, preco
        FROM produtos
        WHERE nome = ?
    '''
    cursor.execute(SQL_BUSCA, (nome,))
    produto = cursor.fetchone()

    if produto:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}")

def apagar_produto(cursor):
    print("###### APAGAR PRODUTO ######")
    ide = input ("Digite o código do produto que deseja apagar: ")

    SQL_DELETE = '''
        DELETE FROM produtos WHERE ide = ?
    '''
    cursor.execute(SQL_DELETE, (ide,))
    print("###### PRODUTO APAGADO COM SUCESSO ######")

def exibir_menu():
    print("Menu principal")
    print("1 - Cadastrar produto")
    print("2 - Estoque total")
    print("3 - Buscar produto")
    print("4 - Apagar produto")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    conn = sqlite3.connect('mercadinho.db')
    cursor = conn.cursor()

    criar_tabela(cursor)

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            cadastrar_produto(cursor)
            conn.commit()
        elif opcao == "2":
            estoque(cursor)
            conn.commit()
        elif opcao == "3":
            busca_produto(cursor)
        elif opcao == "4":
            apagar_produto(cursor)
            conn.commit()
        elif opcao == "0":
            print("###### SESSÃO ENCERRADA ######")
            break
        else:
            print("Opção inválida")

            conn.close()

if __name__ == "__main__":
    main()
