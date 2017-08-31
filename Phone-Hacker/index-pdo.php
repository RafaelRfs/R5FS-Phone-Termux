<?php
/* 
[+]Cria a conexão com o banco de dados
$pdo = new db();
[+]Opcional: 
 $pdo->setTable('users');
[+]Opcional: 
 $pdo->getTable();

[+]Seleciona dados:
$data = $pdo->Read();
$data = $pdo->Read('id = 5');

[+]Insere dados:
$val['nome'] = 'Danilo';
$val['senha'] = '123';
$data = $pdo->Create($val);

[+]Deleta dados:
$id = 3;
$camp = 'id';
$pdo->Delete($id,$camp);
$pdo->Delete($id);

[+]Atualiza dados:
$id = 5;
$val['nome'] = 'Nelson';
$val['senha'] = '123';
$pdo->Update($id,$val,'id');
$pdo->Update($id,$val);

*/

include_once('db.php');
$pdo = new Db();
$data = $pdo->Read();
foreach($data as $dt){
	$txt = '</br>[+]Nome: %s , Senha: %s';
	printf($txt, $dt['nome'], $dt['senha']);
	}
