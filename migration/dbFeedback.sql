create database feedback;

CREATE TABLE tb_comentarios (
	cod_comentario int auto_increment primary key,
    nome varchar(100) not null,
    comentario text not null,
    data_hora datetime not null
);

