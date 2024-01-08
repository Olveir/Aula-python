Utilizando o mesmo padrão do tutorial crie um cadastro de alunos.

A tabela de alunos terá os seguintes campos:

idt
nome
nota1
nota2
numero_faltas


CREATE TABLE aluno(
  idt integer primary key autoincrement,
  nome varchar(50) not null,
  nota1 decimal(3,1) not null,
  nota2 decimal(3,1) not null,
  numero_faltas integer not null);