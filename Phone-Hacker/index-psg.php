<?php 
try{
$pdo = pg_connect('host=localhost  dbname=teste user=root password=""');
$sql = 'select *  from users';
$result = pg_query($pdo, $sql);
print_r(pg_fetch_all($result));
//phpinfo();
}

catch(Exception $e){ 
echo $e;
}
