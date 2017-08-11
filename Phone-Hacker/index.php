<?php 
try{
$pdo = pg_connect('host=localhost dbname=teste user=root password=""');
$sql = 'select *  from users';
$result = pg_query($conn, $sql);
var_dump(pg_fetch_all($result));
}

catch(Exception $e){ 
echo $e;
}
