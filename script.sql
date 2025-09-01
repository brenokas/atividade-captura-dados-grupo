create database oberoncaptura;

use oberoncaptura;

create table capturas(
id int primary key auto_increment,
processamento float,
memoriaRAM float,
memoriaDisco float,
dtCaptura datetime,
nome_usuario varchar(45)
);