# Sistema de Gerenciamento de Biblioteca

Um sistema simples de gerenciamento de livros em uma biblioteca, construído com Python e MySQL.

## Requisitos

- Python 3.7+
- MySQL Server
- pip (gerenciador de pacotes Python)

## Instalação

1. **Clonar ou baixar o projeto**

2. **Criar ambiente virtual:**
   ```bash
   python -m venv venv
   ```

3. **Ativar o ambiente virtual:**
   - Windows PowerShell:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```bash
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar banco de dados:**
   - Abra um client MySQL
   - Execute os comandos do arquivo `schema.sql` para criar as tabelas

6. **Configurar variáveis de ambiente:**
   - Edite o arquivo `.env` com suas credenciais do MySQL:
     ```
     DB_HOST=localhost
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_NAME=biblioteca
     ```

## Uso

Execute o programa:
```bash
python biblioteca.py
```

### Funcionalidades

1. **Cadastrar novo livro** - Adicione um novo livro ao acervo da biblioteca
2. **Buscar livro por título** - Procure livros pelo título
3. **Listar todos os livros** - Visualize todos os livros cadastrados
4. **Atualizar dados do livro** - Modifique informações de um livro existente
5. **Deletar livro** - Remova um livro do acervo
6. **Sair** - Encerre o programa

## Estrutura do Banco de Dados

### Tabela: livros
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INT | Identificador único (chave primária) |
| titulo | VARCHAR(255) | Título do livro |
| autor | VARCHAR(255) | Autor do livro |
| ano_publicacao | INT | Ano de publicação |
| categoria | VARCHAR(100) | Categoria/gênero do livro |
| created_at | TIMESTAMP | Data de criação do registro |
| updated_at | TIMESTAMP | Data da última atualização |

## Dependências

- `mysql-connector-python` - Conector MySQL para Python
- `python-dotenv` - Carregador de variáveis de ambiente

## Desativar ambiente virtual

Quando terminar, desative o ambiente virtual:
```bash
deactivate
```

## Autor

Projeto integrador - Técnico de Informática para Internet
