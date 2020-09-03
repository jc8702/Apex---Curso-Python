CREATE DATABASE livraria;
USE livraria;
# 1. Um livro pode possuir mais de 1 autor.
# livro: 1 -> autor: N
# autor: 1 -> livro: N
# autor: N -> livro: N

CREATE TABLE livros(
	id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    PRIMARY KEY(id));
    
CREATE TABLE autores(
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KEY(id));

# Temos que criar essa tabela associativa, pois estamos trabalhando com um relacionamento do tipo muitos para muitos.
CREATE TABLE autores_livros(
	id_livro INT NOT NULL,
    id_autor INT NOT NULL,
    PRIMARY KEY(id_livro, id_autor),
    FOREIGN KEY (id_livro) REFERENCES livros(id),
    FOREIGN KEY (id_autor) REFERENCES autores(id));

# Inserindo alguns autores no banco
INSERT INTO autores(nome) VALUES ('J.R.R Tolkien');
INSERT INTO autores(nome) VALUES ('H.P Lovecraft');

# Inserindo alguns livros no banco
INSERT INTO livros(titulo) VALUES ('The Lord of the Rings');
INSERT INTO livros(titulo) VALUES('The Hobbit');
INSERT INTO livros(titulo) VALUES ('The Call of Cthulhu');

# Aqui associamos os livros que foram cadastrados aos autores
INSERT INTO autores_livros(id_livro, id_autor)
VALUES(1, 1);
INSERT INTO autores_livros(id_livro, id_autor)
VALUES(2, 1);
INSERT INTO autores_livros(id_livro, id_autor)
VALUES(3, 2);

SELECT * FROM autores;
SELECT * FROM livros;
SELECT * FROM autores_livros;

# Com esse join, conseguimos visualizar os dados das tabelas relacionadas, nesse caso, nome do autor e título do livro.
CREATE VIEW autores_e_livros
AS
SELECT autores.nome, livros.titulo FROM autores
INNER JOIN autores_livros ON autores.id = autores_livros.id_autor
INNER JOIN livros ON livros.id = autores_livros.id_livro;

SELECT * FROM autores_e_livros;

# 2. Um livro deve possuir uma categoria e podem existir vários livros com uma mesma categoria.
# livro 1 : 1 categoria
# categoria 1 : n livro
# Uma categoria pode estar em vários livros, porém um livro possui apenas uma categoria.
CREATE TABLE categorias(
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100),
    PRIMARY KEY(id));

ALTER TABLE livros ADD id_categoria INT;
ALTER TABLE livros ADD FOREIGN KEY(id_categoria)
REFERENCES categorias(id);
DESC livros;
INSERT INTO categorias(nome) VALUES ('Fantasia');
INSERT INTO categorias(nome) VALUES ('Cosmic Horror');

SELECT * FROM categorias;
SELECT * FROM livros;

UPDATE livros SET id_categoria = 2 WHERE id IN (1, 2);
UPDATE livros SET id_categoria = 1 WHERE id IN (3);


# 3. Podem ser atribuídas várias tags para um determinado livro e uma tag pode estar associada a vários livros


# 4. A livraria deve possuir um cadastro de seus associados


# 5. Cada associado pode alugar um ou mais livros durante uma única locação
# 6. O valor de cada locação será definido pela quantidade de livros retirados, e todos os livros possuem o mesmo valor de locação. Entretanto, o valor de locação de um livro pode mudar em períodos distintos
# 7. Livros do mesmo ISBN devem possuir um código sequencial para diferenciá-los.
