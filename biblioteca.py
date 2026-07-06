# importa a bilioteca que permite o python se comunicar com o sistema operacional
import os
# importa a biblioteca que permite o python se comunicar com o banco de dados MySQL
import mysql.connector
# importa a biblioteca que permite o python ler variáveis de ambiente de um arquivo .env
from dotenv import load_dotenv
# carrega as variáveis de ambiente do arquivo .env
load_dotenv()
# lê as variáveis de ambiente do arquivo .env
host_banco = os.getenv("DB_HOST")
usuario_banco = os.getenv("DB_USER")
senha_banco = os.getenv("DB_PASSWORD")
nome_banco = os.getenv("DB_NAME")
# verifica se todas as variáveis de ambiente foram carregadas corretamente
if not all([host_banco, usuario_banco, senha_banco, nome_banco]):
    raise ValueError("Variaveis ausentes no arquivo .env. Por favor, verifique se todas as variaveis de ambiente estão definidas corretamente.")
# define a classe Livro com os atributos id, titulo, autor, ano_publicacao e categoria
class Livro:
    def __init__(self, id, titulo, autor, ano_publicacao, categoria):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.categoria = categoria

    def __str__(self):
        return f'[{self.id}] {self.titulo} - {self.autor} | Ano: {self.ano_publicacao} | Categoria: {self.categoria}'

# Insere um novo livro no banco de dados
def cadastrar(conexao, cursor):
    print('\n--- Cadastrar novo livro ---')
    titulo = input('Título do livro: ')
    autor = input('Autor: ')
    ano_publicacao = input('Ano de publicação: ')
    categoria = input('Categoria: ')
    cursor.execute(
        'INSERT INTO livros (titulo, autor, ano_publicacao, categoria) VALUES (%s, %s, %s, %s)',
        (titulo, autor, ano_publicacao, categoria)
    )
    conexao.commit()
    print('Livro cadastrado com sucesso!')

# Busca um livro pelo título
def buscar(cursor):
    titulo = input('Digite o título do livro: ')
    cursor.execute('SELECT * FROM livros WHERE titulo LIKE %s', (f'%{titulo}%',))
    resultado = cursor.fetchall()
    if resultado:
        for livro in resultado:
            print(livro)
    else:
        print('Livro não encontrado.')

# Lista todos os livros cadastrados
def listar(cursor):
    cursor.execute('SELECT * FROM livros')
    resultado = cursor.fetchall()
    if resultado:
        for livro in resultado:
            print(livro)
    else:
        print('Nenhum livro cadastrado.')

# Atualiza os dados de um livro existente
def atualizar(conexao, cursor):
    print('\n--- Atualizar dados do livro ---')
    livro_id = input('ID do livro a atualizar: ')
    cursor.execute('SELECT * FROM livros WHERE id = %s', (livro_id,))
    if not cursor.fetchall():
        print('Livro não encontrado.')
        return
    
    print('Deixe em branco para não alterar um campo')
    titulo = input('Novo título (ou deixe em branco): ')
    autor = input('Novo autor (ou deixe em branco): ')
    ano_publicacao = input('Novo ano de publicação (ou deixe em branco): ')
    categoria = input('Nova categoria (ou deixe em branco): ')
    
    campos_atualizar = []
    valores = []
    
    if titulo:
        campos_atualizar.append('titulo = %s')
        valores.append(titulo)
    if autor:
        campos_atualizar.append('autor = %s')
        valores.append(autor)
    if ano_publicacao:
        campos_atualizar.append('ano_publicacao = %s')
        valores.append(ano_publicacao)
    if categoria:
        campos_atualizar.append('categoria = %s')
        valores.append(categoria)
    
    # Se houver campos para atualizar, executa a query
    if campos_atualizar:
        valores.append(livro_id)
        query = f"UPDATE livros SET {', '.join(campos_atualizar)} WHERE id = %s"
        cursor.execute(query, tuple(valores))
        conexao.commit()
        print('Livro atualizado com sucesso!')
    else:
        print('Nenhum campo foi alterado.')

# Deleta um livro do banco de dados
def deletar(conexao, cursor):
    print('\n--- Deletar livro ---')
    livro_id = input('ID do livro a deletar: ')
    cursor.execute('SELECT * FROM livros WHERE id = %s', (livro_id,))
    if not cursor.fetchall():
        print('Livro não encontrado.')
        return
    
    confirmacao = input('Tem certeza que deseja deletar este livro? (s/n): ')
    if confirmacao.lower() == 's':
        cursor.execute('DELETE FROM livros WHERE id = %s', (livro_id,))
        conexao.commit()
        print('Livro deletado com sucesso!')
    else:
        print('Operação cancelada.')

# Menu principal com opções de CRUD
def menu():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host=host_banco,
            user=usuario_banco,
            password=senha_banco,
            database=nome_banco
        )
        cursor = conexao.cursor()

        while True:
            print('\n=== Sistema de Gerenciamento de Biblioteca ===')
            print('1. Cadastrar novo livro')
            print('2. Buscar livro por título')
            print('3. Listar todos os livros')
            print('4. Atualizar dados do livro')
            print('5. Deletar livro')
            print('0. Sair')
            opcao = input('Escolha uma opção: ')
            match opcao:
                case '1':
                    cadastrar(conexao,cursor)
                case '2':
                    buscar(cursor)
                case '3':
                    listar(cursor)
                case '4':
                    atualizar(conexao,cursor)
                case '5':
                    deletar(conexao,cursor)
                case '0':
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")        
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    finally:
         if cursor is not None:
            cursor.close()
         if conexao is not None and conexao.is_connected():
            conexao.close()

if __name__ == "__main__":
    menu()