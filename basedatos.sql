CREATE DATABASE IF NOT EXISTS pi_docker;
use pi_docker;

CREATE TABLE Usuarios(
id_usuario int(10) auto_increment not null,
nombre varchar(30),
username varchar(15),
passwd varchar(64),
CONSTRAINT pk_usuario PRIMARY KEY(id_usuario),
CONSTRAINT uq_username UNIQUE(username)
)ENGINE=InnoDb;