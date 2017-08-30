<?php
$pdo = new PDO('pgsql:host=localhost;dbname=postgres','username','');
$sql = "SELECT * FROM users";
$query = $pdo->query($sql);
$query->setFetchMode(PDO::FETCH_ASSOC);
$data = $query->fetchAll();

foreach($data as $dt){
	$txt = '</br>[+]Nome: %s , Senha: %s';
	printf($txt, $dt['nome'], $dt['senha']);
	}


$sql =  'insert into users(nome,senha) values(?,?)';
$query = $pdo->prepare($sql);
$query->bindValue(1,'Daniel',PDO::PARAM_STR);
$query->bindValue(2,'123',PDO::PARAM_STR);
$query->execute();

