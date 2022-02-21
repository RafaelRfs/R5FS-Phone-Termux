<?php 

$files = file('gems3.txt');
foreach($files as $file){
	$str = strip_tags(trim($file));
	if($str <> ''){
		$pr = array('(',')','~','>','(~>','ï»¿','=','ï»¿',',','<');
		$sti =  str_replace($pr,'',$str);
		$val = explode(" ",$sti); 
		while($chave = array_search('', $val)){ unset($val[$chave]);}
		$gem = strip_tags(trim($val[0]));
		$versao = isset($val[1]) && strip_tags(trim($val[1]) <> '')? " -v ".$val[1] : '';
		$versao2 = isset($val[2]) && strip_tags(trim($val[2]) <> '')? " -v ".$val[2] : '';
		$install = 'sudo gem install ';
		if($versao == '' && $versao2 == ''){
			echo $install.$gem.'<br/>';
			}else{
				if($versao <> ''){
					echo $install.$gem.$versao.'<br/>';
					}
				if($versao2 <> ''){
					echo $install.$gem.$versao2.'<br/>';
					}		
				}
		}
	}