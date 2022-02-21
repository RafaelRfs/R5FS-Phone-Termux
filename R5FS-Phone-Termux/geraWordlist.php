<?php

class geraWordlist{
	private $wrd,$pass,$attempts = 15320,$fat = 1,$values,$inf = 0;
	
    public function __construct($wrd){
		$this->wrd = $wrd;
		
		}
		
	public function Run(){
		$this->values = array();
		$this->setFat();
		$this->setComb();
		}	
		
	public function getWrd(){ return $this->wrd;}
	public function getInf(){ return $this->inf;}	
	public function setInf($inf){$this->inf = $inf;}
	public function setAttempts($at){ $this->attempts = $at;}
	public function getAttempts(){return $this->$this->attempts();}
	
	public function setPass($ps){ 
	$this->pass = $ps; 
	$this->Run();
	$this->setCombPass();
	}
	public function getPass(){return $this->pass;}
	public function setFat(){
		$count = strlen($this->wrd);
		$num = 1;
		$values = array();
		for($i = $count; $i > 0 ; $i--){
		$this->fat *=$i;
		}
	}
	
	public function getFat(){return $this->fat;}
	
	public function setComb(){
		$this->values[] = $this->wrd;
		for($i = 0; $i  < $this->getFat() ; $i++){
		$val = str_shuffle($this->wrd);
		while(in_array($val, $this->values)){
		$val = str_shuffle($this->wrd);
		}
		$this->values[] = $val;
		if($i ==  $this->attempts && $this->inf == 0){ break;}
		}//Fecha o For
		}//Combinações
	
	public function setCombPass(){
		$i = 1;
		foreach($this->values as $val){
		if($val == $this->pass){
		echo "\n[+]".$i." Attempts {Password Cracked}  => ".$val."\n\n";
		break;
		}
		$i++;
		}//Fecha o For
		
	}//Fecha o comb PAsss
	
	 public function getComb(){ return $this->values;}
	
	}//Fecha a class