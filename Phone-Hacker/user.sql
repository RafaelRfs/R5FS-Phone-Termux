CREATE TABLE IF NOT EXISTS users (id serial primary key, nome text not null ,senha text not null);
insert into users(nome,senha) values('Rafael','123'),('Will','123');
