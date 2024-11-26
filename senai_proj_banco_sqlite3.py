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
    print("Preencha os dados do produto:")
    nome = input("ITEM: ")
    quantidade = input("QUANT.: ")
    preco = input("PRECO: ")

    SQL_INSERT = ''' 
        INSERT INTO produtos(nome, quantidade, preco) 
        VALUES (?, ?, ?)
    '''
    cursor.execute(SQL_INSERT, (nome, quantidade, preco))
    print("Produto cadastrado com sucesso")

def estoque_total(cursor):
    print("Produtos em estoque:")
    SQL_ESTOQUE = '''
        SELECT nome as "Nome do produto", quantidade as "Quantidade em estoque", preco as "Preço"
        FROM produtos
    '''
    cursor.execute(SQL_ESTOQUE)
    produto = cursor.fetchall()

    if produto:
        print(produto)
        # print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}" )

def busca_produto(cursor):
    nome = input("Digite o nome do produto: ")
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
    print("APAGAR PRODUTO")
    nome = input ("Digite o nome do produto que deseja apagar: ")

    SQL_DELETE = '''
        DELETE FROM produtos WHERE nome = ?
    '''
    cursor.execute(SQL_DELETE, (nome,))
    print("Produto apagado com sucesso")

def exibir_menu():
    print("Menu principal")
    print("1 - Cadastrar produto")
    print("2 - Estoque total")
    print("3 - Buscar produto")
    print("4 - Apagar produto")
    print("ESC - Sair")
    return input("Escolha uma opção: ")

def main():
    conn = sqlite3.connect('mercadinho.db')
    cursor = conn.cursor()

    criar_tabela(cursor)

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            print("##### CADASTRO DE PRODUTO #####")
            cadastrar_produto(cursor)
            conn.commit()
        elif opcao == "2":
            print("##### ESTOQUE TOTAL #####")
            estoque_total(cursor)
            conn.commit()
        elif opcao == "3":
            busca_produto(cursor)
        elif opcao == "4":
            apagar_produto(cursor)
            conn.commit()
        elif opcao == "ESC":
            print("##### SESSÃO ENCERRADA #####")
            break
        else:
            print("Opção inválida")

            conn.close()

if __name__ == "__main__":
    main()
