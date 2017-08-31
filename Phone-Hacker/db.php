<?php
define('USERNAME', 'username');
define('PASS','');
define('HOST','localhost');
define('DBNAME','postgres');
define('TYPE','pgsql');

class Db {	
private $db, $table = 'users' ;

public function __construct(){
	$this->getConn();
	}
	
private function getConn(){
try{	
if(is_null($this->db)){
$this->db = new PDO(TYPE.':host='.HOST.';dbname='.DBNAME,USERNAME,PASS);
}
}catch(Exception $e){
echo $e;
return '';	
}
}//database connection

public function setTable($table){
	$this->table = $table;
	}
	
public function getTable(){ return $this->table;}
	
private function getStr($data){
	$dt =  array();
	$indices = array_keys($data);
	$dt['ind'] = $indices;
	$count = count($indices);
	$dt['count'] = $count; 
    $num = 0;
    $dt['str'] = '';
	$dt['qst'] = '';
    $dt['cmb'] = '';
    foreach($indices as $ind){
	$dt['str'] .=$ind;
	$dt['qst'] .='?';
	$dt['cmb'] .= $ind.'=?';
	if($num+1 < $count){ 
	$dt['str'] .=','; 
	$dt['qst'] .=',';
	$dt['cmb'] .=',';
	}
	$num++;
	}//Fecha o Foreach
	return $dt;
	}
		
private function Prepare($pdo, $dta,$dx){
	$count = $dx['count'];
	$count2 = count($dta);
	if($count == $count2){
      for($i = 0; $i < $count ; $i++){
		  $v = $i + 1 ;
	      $pdo->bindValue($v, $dta[$dx['ind'][$i]], PDO::PARAM_STR);
		}
	$pdo->execute();  
	}
	}//Private function 	
	
public function Create($data){
	$dt = $this->getStr($data);
	$sql = 'INSERT INTO '.$this->table.'('.$dt['str'].') Values('.$dt['qst'].')';
	$pdo = $this->db->prepare($sql);
	$this->Prepare($pdo,$data,$dt);
    }// INSERT INTOOOOO

public function Read($where = ''){
	$sql = 'SELECT * FROM '.$this->table;
	$sql = strip_tags(trim($where == ''))? $sql : $sql.' WHERE '.$where;
	$pdo = $this->db->query($sql);
	$pdo->setFetchMode(PDO::FETCH_ASSOC);
	return $pdo->fetchAll();
	}
	
public function Update($id,$data,$camp = 'id'){
	$dt =  $this->getStr($data);
	var_dump($dt);
	$sql = 'UPDATE '.$this->table.' SET '.$dt['cmb'].' WHERE '.$camp.'='.$id;
	$pdo = $this->db->prepare($sql);
	echo $sql;
	$this->Prepare($pdo,$data,$dt);
	}
	
public function Delete($id,$camp='id'){
	$sql = 'DELETE FROM '.$this->table.' WHERE '.$camp.'='.$id;
	$pdo = $this->db->query($sql);
	}	
		
}//Classe do Bd Louco