CREATE DATABASE loja;

USE loja;

CREATE TABLE cliente (
    cliente_id INT,
    endereco VARCHAR(30),
    nome VARCHAR(30),
    idade INT
);
 
CREATE TABLE pedido (
    pedido_id INT,
    pedido INT,
    endereco VARCHAR(30),
    nome VARCHAR(30)
)

SELECT c.nome, p.pedido_id
FROM cliente c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id;

SELECT c.nome, p.pedido_id
FROM pedidos p
LEFT JOIN cliente c ON c.cliente_id = p.cliente_id;
	
