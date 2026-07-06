-- Criar banco de dados (se não existir)
CREATE DATABASE IF NOT EXISTS biblioteca;

-- Usar o banco de dados
USE biblioteca;

-- Criar tabela de gêneros (se não existir)
CREATE TABLE IF NOT EXISTS genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Criar tabela de livros (se não existir)
CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(80) NOT NULL,
    autor VARCHAR(80) NOT NULL,
    ano_publicacao INT,
    categoria VARCHAR(50),
    genero_id INT,
    CONSTRAINT fk_livros_genero FOREIGN KEY (genero_id) REFERENCES genero(id)
);