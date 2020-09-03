# Criando uma nova tabela
CREATE TABLE clientes(id INT, nome VARCHAR(100));

# Adicionar uma nova coluna a tabela
ALTER TABLE clientes ADD idade TINYINT;

# Modificar o tipo da coluna
ALTER TABLE clientes MODIFY idade INT;

# Remover uma coluna
ALTER TABLE clientes DROP idade;

# Modificar o nome da coluna
ALTER TABLE clientes CHANGE nome nome_completo VARCHAR(100);

# Modificar o nome da tabela
ALTER TABLE clientes RENAME TO usuarios;

# ALTER TABLE usuarios MODIFY id INT(11) NOT NULL;

# Inserindo dados na tabela
# CRUD -> C = Create
INSERT INTO usuarios VALUES();
INSERT INTO usuarios VALUES(1, 'Maria das Dores', 21);
INSERT INTO usuarios VALUES(2, 'João das Dores', 39);
INSERT INTO usuarios VALUES(3, 'Paulo das Dores', 60);


# Visualizando todos os dados da tabela
# CRUD -> R = Retrieve
SELECT * FROM usuarios;
SELECT nome_completo, idade FROM usuarios;

# Alterando registros
# CRUD -> U = Update
SET SQL_SAFE_UPDATES = 0;
UPDATE usuarios SET nome_completo = 'Fulano' WHERE id = 1;

# Excluindo registros
# CRUD -> D = Delete
DELETE FROM usuarios;
DELETE FROM usuarios WHERE id = 1;

# Operadores
# Comparação
# =, >, <, >=, <=, <>
SELECT * FROM city WHERE Population >= 1000000;
SELECT * FROM city WHERE Population < 1000;
SELECT * FROM city WHERE CountryCode <> 'USA';

# Lógicos
# AND, BETWEEN, IN/NOT IN (IN ('Paris', 'London')), LIKE/NOT LIKE ('s%'), OR
# AND
SELECT * FROM city WHERE CountryCode = 'RUS' AND Population >= 1000000;

# OR
SELECT * FROM city WHERE CountryCode = 'CHN' OR CountryCode = 'USA';
# IN
SELECT * FROM city WHERE CountryCode IN ('ZWE', 'EST');
SELECT * FROM city WHERE CountryCode NOT IN ('USA', 'BRA');

# BETWEEN
SELECT * FROM city WHERE id BETWEEN 1200 AND 1210;

# LIKE
SELECT * FROM city WHERE Name LIKE('%chi%') AND id BETWEEN 1200 AND 1210;

# Matemáticos
# +, -, *, /, %

SELECT 3 + 3 AS 'Soma', 20/4 AS 'Divisão';
SELECT Population * 1000000 FROM city;

CREATE TABLE clientes(id INT NOT NULL, nome VARCHAR(100) NULL DEFAULT('Anônimo'), idade INT);
INSERT INTO clientes(id) VALUES (1);
INSERT INTO clientes(id, nome) VALUES (2, 'Pedro');

# ------------------------------------------------------
# sakila
# https://dev.mysql.com/doc/refman/8.0/en/string-functions.html
# substring, len, lower, concat

SELECT * FROM address;
SELECT * FROM category;

SELECT LOWER(first_name), UPPER(last_name) FROM customer;
SELECT LENGTH(first_name) FROM customer;
SELECT SUBSTRING('Alessandro', 1, 3);
SELECT CONCAT(first_name, ' 666 ', last_name) FROM customer;
SELECT FORMAT(120.2957438573485, 2);
# trim, rtrim, ltrim
SELECT length(trim(' SD '));

SELECT COUNT(*) FROM payment;
SELECT MIN(amount) FROM payment;
select SUM(amount) FROM payment;

SELECT DISTINCT amount FROM payment;

CREATE TABLE sales
(
    year    INT,
    country VARCHAR(30),
    product VARCHAR(32),
    profit  INT
);

DROP TABLE sales;

INSERT INTO sales VALUES(2010, "Brazil", "Computer", 1984);
INSERT INTO sales VALUES(2010, "Brazil", "TV", 2743);
INSERT INTO sales VALUES(2010, "Brazil", "Cellphone", 2990);
INSERT INTO sales VALUES(2010, "China", "Computer", 4105);
INSERT INTO sales VALUES(2010, "China", "TV", 3605);
INSERT INTO sales VALUES(2010, "China", "Cellphone", 2090);
INSERT INTO sales VALUES(2010, "Russia", "Computer", 2194);
INSERT INTO sales VALUES(2010, "Russia", "TV", 2990);
INSERT INTO sales VALUES(2010, "Russia", "Cellphone", 1006);
INSERT INTO sales VALUES(2010, "United States of America", "Computer", 4669);
INSERT INTO sales VALUES(2010, "United States of America", "TV", 1859);
INSERT INTO sales VALUES(2010, "United States of America", "Cellphone", 3965);
INSERT INTO sales VALUES(2010, "France", "Computer", 3114);
INSERT INTO sales VALUES(2010, "France", "TV", 4416);
INSERT INTO sales VALUES(2010, "France", "Cellphone", 4518);
INSERT INTO sales VALUES(2011, "Brazil", "Computer", 1053);
INSERT INTO sales VALUES(2011, "Brazil", "TV", 1167);
INSERT INTO sales VALUES(2011, "Brazil", "Cellphone", 2403);
INSERT INTO sales VALUES(2011, "China", "Computer", 4529);
INSERT INTO sales VALUES(2011, "China", "TV", 4411);
INSERT INTO sales VALUES(2011, "China", "Cellphone", 2702);
INSERT INTO sales VALUES(2011, "Russia", "Computer", 2238);
INSERT INTO sales VALUES(2011, "Russia", "TV", 3633);
INSERT INTO sales VALUES(2011, "Russia", "Cellphone", 1953);
INSERT INTO sales VALUES(2011, "United States of America", "Computer", 3327);
INSERT INTO sales VALUES(2011, "United States of America", "TV", 2936);
INSERT INTO sales VALUES(2011, "United States of America", "Cellphone", 3168);
INSERT INTO sales VALUES(2011, "France", "Computer", 3752);
INSERT INTO sales VALUES(2011, "France", "TV", 2257);
INSERT INTO sales VALUES(2011, "France", "Cellphone", 2094);
INSERT INTO sales VALUES(2012, "Brazil", "Computer", 4760);
INSERT INTO sales VALUES(2012, "Brazil", "TV", 3822);
INSERT INTO sales VALUES(2012, "Brazil", "Cellphone", 3435);
INSERT INTO sales VALUES(2012, "China", "Computer", 1286);
INSERT INTO sales VALUES(2012, "China", "TV", 2751);
INSERT INTO sales VALUES(2012, "China", "Cellphone", 1662);
INSERT INTO sales VALUES(2012, "Russia", "Computer", 2902);
INSERT INTO sales VALUES(2012, "Russia", "TV", 1646);
INSERT INTO sales VALUES(2012, "Russia", "Cellphone", 2425);
INSERT INTO sales VALUES(2012, "United States of America", "Computer", 3117);
INSERT INTO sales VALUES(2012, "United States of America", "TV", 4455);
INSERT INTO sales VALUES(2012, "United States of America", "Cellphone", 3711);
INSERT INTO sales VALUES(2012, "France", "Computer", 4753);
INSERT INTO sales VALUES(2012, "France", "TV", 1018);
INSERT INTO sales VALUES(2012, "France", "Cellphone", 3466);
INSERT INTO sales VALUES(2013, "Brazil", "Computer", 1509);
INSERT INTO sales VALUES(2013, "Brazil", "TV", 4359);
INSERT INTO sales VALUES(2013, "Brazil", "Cellphone", 2947);
INSERT INTO sales VALUES(2013, "China", "Computer", 3329);
INSERT INTO sales VALUES(2013, "China", "TV", 2289);
INSERT INTO sales VALUES(2013, "China", "Cellphone", 3949);
INSERT INTO sales VALUES(2013, "Russia", "Computer", 4896);
INSERT INTO sales VALUES(2013, "Russia", "TV", 3075);
INSERT INTO sales VALUES(2013, "Russia", "Cellphone", 1793);
INSERT INTO sales VALUES(2013, "United States of America", "Computer", 2225);
INSERT INTO sales VALUES(2013, "United States of America", "TV", 1436);
INSERT INTO sales VALUES(2013, "United States of America", "Cellphone", 1541);
INSERT INTO sales VALUES(2013, "France", "Computer", 2430);
INSERT INTO sales VALUES(2013, "France", "TV", 3908);
INSERT INTO sales VALUES(2013, "France", "Cellphone", 4716);
INSERT INTO sales VALUES(2014, "Brazil", "Computer", 1919);
INSERT INTO sales VALUES(2014, "Brazil", "TV", 4949);
INSERT INTO sales VALUES(2014, "Brazil", "Cellphone", 1697);
INSERT INTO sales VALUES(2014, "China", "Computer", 1475);
INSERT INTO sales VALUES(2014, "China", "TV", 2630);
INSERT INTO sales VALUES(2014, "China", "Cellphone", 1728);
INSERT INTO sales VALUES(2014, "Russia", "Computer", 2102);
INSERT INTO sales VALUES(2014, "Russia", "TV", 2074);
INSERT INTO sales VALUES(2014, "Russia", "Cellphone", 4402);
INSERT INTO sales VALUES(2014, "United States of America", "Computer", 1118);
INSERT INTO sales VALUES(2014, "United States of America", "TV", 3483);
INSERT INTO sales VALUES(2014, "United States of America", "Cellphone", 4426);
INSERT INTO sales VALUES(2014, "France", "Computer", 3326);
INSERT INTO sales VALUES(2014, "France", "TV", 3082);
INSERT INTO sales VALUES(2014, "France", "Cellphone", 2441);
INSERT INTO sales VALUES(2015, "Brazil", "Computer", 1719);
INSERT INTO sales VALUES(2015, "Brazil", "TV", 3187);
INSERT INTO sales VALUES(2015, "Brazil", "Cellphone", 2808);
INSERT INTO sales VALUES(2015, "China", "Computer", 4414);
INSERT INTO sales VALUES(2015, "China", "TV", 4614);
INSERT INTO sales VALUES(2015, "China", "Cellphone", 3916);
INSERT INTO sales VALUES(2015, "Russia", "Computer", 4212);
INSERT INTO sales VALUES(2015, "Russia", "TV", 2959);
INSERT INTO sales VALUES(2015, "Russia", "Cellphone", 1346);
INSERT INTO sales VALUES(2015, "United States of America", "Computer", 4739);
INSERT INTO sales VALUES(2015, "United States of America", "TV", 3078);
INSERT INTO sales VALUES(2015, "United States of America", "Cellphone", 4550);
INSERT INTO sales VALUES(2015, "France", "Computer", 3758);
INSERT INTO sales VALUES(2015, "France", "TV", 3554);
INSERT INTO sales VALUES(2015, "France", "Cellphone", 4970);
INSERT INTO sales VALUES(2016, "Brazil", "Computer", 4550);
INSERT INTO sales VALUES(2016, "Brazil", "TV", 1270);
INSERT INTO sales VALUES(2016, "Brazil", "Cellphone", 4482);
INSERT INTO sales VALUES(2016, "China", "Computer", 4787);
INSERT INTO sales VALUES(2016, "China", "TV", 4887);
INSERT INTO sales VALUES(2016, "China", "Cellphone", 3524);
INSERT INTO sales VALUES(2016, "Russia", "Computer", 1412);
INSERT INTO sales VALUES(2016, "Russia", "TV", 4410);
INSERT INTO sales VALUES(2016, "Russia", "Cellphone", 4266);
INSERT INTO sales VALUES(2016, "United States of America", "Computer", 2326);
INSERT INTO sales VALUES(2016, "United States of America", "TV", 1208);
INSERT INTO sales VALUES(2016, "United States of America", "Cellphone", 4175);
INSERT INTO sales VALUES(2016, "France", "Computer", 2945);
INSERT INTO sales VALUES(2016, "France", "TV", 2558);
INSERT INTO sales VALUES(2016, "France", "Cellphone", 3639);
INSERT INTO sales VALUES(2017, "Brazil", "Computer", 3421);
INSERT INTO sales VALUES(2017, "Brazil", "TV", 3028);
INSERT INTO sales VALUES(2017, "Brazil", "Cellphone", 4504);
INSERT INTO sales VALUES(2017, "China", "Computer", 4763);
INSERT INTO sales VALUES(2017, "China", "TV", 1631);
INSERT INTO sales VALUES(2017, "China", "Cellphone", 2160);
INSERT INTO sales VALUES(2017, "Russia", "Computer", 1929);
INSERT INTO sales VALUES(2017, "Russia", "TV", 3836);
INSERT INTO sales VALUES(2017, "Russia", "Cellphone", 2238);
INSERT INTO sales VALUES(2017, "United States of America", "Computer", 4483);
INSERT INTO sales VALUES(2017, "United States of America", "TV", 2483);
INSERT INTO sales VALUES(2017, "United States of America", "Cellphone", 3506);
INSERT INTO sales VALUES(2017, "France", "Computer", 1303);
INSERT INTO sales VALUES(2017, "France", "TV", 1390);
INSERT INTO sales VALUES(2017, "France", "Cellphone", 2819);
INSERT INTO sales VALUES(2018, "Brazil", "Computer", 4573);
INSERT INTO sales VALUES(2018, "Brazil", "TV", 3750);
INSERT INTO sales VALUES(2018, "Brazil", "Cellphone", 4682);
INSERT INTO sales VALUES(2018, "China", "Computer", 3234);
INSERT INTO sales VALUES(2018, "China", "TV", 4468);
INSERT INTO sales VALUES(2018, "China", "Cellphone", 1546);
INSERT INTO sales VALUES(2018, "Russia", "Computer", 2143);
INSERT INTO sales VALUES(2018, "Russia", "TV", 1717);
INSERT INTO sales VALUES(2018, "Russia", "Cellphone", 3207);
INSERT INTO sales VALUES(2018, "United States of America", "Computer", 1419);
INSERT INTO sales VALUES(2018, "United States of America", "TV", 3700);
INSERT INTO sales VALUES(2018, "United States of America", "Cellphone", 1266);
INSERT INTO sales VALUES(2018, "France", "Computer", 2685);
INSERT INTO sales VALUES(2018, "France", "TV", 4791);
INSERT INTO sales VALUES(2018, "France", "Cellphone", 1255);
INSERT INTO sales VALUES(2019, "Brazil", "Computer", 3682);
INSERT INTO sales VALUES(2019, "Brazil", "TV", 1912);
INSERT INTO sales VALUES(2019, "Brazil", "Cellphone", 2743);
INSERT INTO sales VALUES(2019, "China", "Computer", 2548);
INSERT INTO sales VALUES(2019, "China", "TV", 3639);
INSERT INTO sales VALUES(2019, "China", "Cellphone", 1923);
INSERT INTO sales VALUES(2019, "Russia", "Computer", 1604);
INSERT INTO sales VALUES(2019, "Russia", "TV", 2782);
INSERT INTO sales VALUES(2019, "Russia", "Cellphone", 2794);
INSERT INTO sales VALUES(2019, "United States of America", "Computer", 2125);
INSERT INTO sales VALUES(2019, "United States of America", "TV", 1570);
INSERT INTO sales VALUES(2019, "United States of America", "Cellphone", 1112);
INSERT INTO sales VALUES(2019, "France", "Computer", 4268);
INSERT INTO sales VALUES(2019, "France", "TV", 3612);
INSERT INTO sales VALUES(2019, "France", "Cellphone", 2397);

SELECT * FROM sales;

SELECT year, country, product, SUM(profit) AS profit
       FROM sales
       GROUP BY year, country, product;
       
SELECT date_add('2000-01-12', INTERVAL 10 YEAR);
SELECT month(curdate());

SELECT city_id, city, country_id, date_format(last_update, '%d-%m-%Y') as last_update FROM city;

SELECT year(now());

CREATE table Teste(id INT NOT NULL AUTO_INCREMENT, numero INT NOT NULL, PRIMARY KEY(id));
CREATE table Teste(id INT NOT NULL, numero INT NOT NULL);
ALTER TABLE Teste CHANGE id id INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Teste ADD PRIMARY KEY(id);
DROP TABLE Teste;
DESC Teste;
SELECT * FROM Teste;
INSERT INTO Teste(numero) VALUES (1);

SELECT CountryCode, sum(Population) soma FROM city GROUP BY CountryCode ORDER BY Countrycode;

SELECT sum(Population) FROM city WHERE CountryCode = 'BRA';

SELECT CAST('122' AS DECIMAL);
# ---------------

SELECT * FROM film;