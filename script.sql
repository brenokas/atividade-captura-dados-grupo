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

CREATE USER 'userOberon'@'%' IDENTIFIED BY 'Urubu100#';

GRANT ALL PRIVILEGES ON oberoncaptura.* TO 'userOberon'@'%';

flush privileges;

select * from capturas;

select processamento, dtCaptura from capturas;

SELECT * FROM capturas where nome_usuario = 'brenokas';