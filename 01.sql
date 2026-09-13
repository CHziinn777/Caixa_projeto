Use mercado_database;

create table produtos (
    id int primary key auto_increment,
    nome varchar(100) not null,
    preco decimal(10,2) not null,
    quantidade int not null
);

select * 
from produtos;

insert into produtos (nome, preco, quantidade)
values ('Arroz', 18.50, 34);