CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    num_matricula INT,
    endereco VARCHAR(30),
    nome VARCHAR(30),
    idade INT
);
 
CREATE TABLE professores (
    num_matricula INT,
    endereco VARCHAR(30),
    especialidade VARCHAR(30),
    nome VARCHAR(30),
    idade INT
);

CREATE TABLE turma (
	inicio_aula INT,
	termino_aula INT,
	dia_semana VARCHAR(30)
);

CREATE TABLE diciplina (
    id_curso INT,
    nome_curso VARCHAR(30),
    carga_horaria INT,
    quant_aulas INT
);

CREATE TABLE matriculas (
id_matricula INT,
id_aluno INT,
data_matricula DATE
);

drop table matriculas