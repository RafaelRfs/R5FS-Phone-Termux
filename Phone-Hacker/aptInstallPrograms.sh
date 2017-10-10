echo "______________________________________________"
echo "[+]Instando o The Harvester..."
echo "______________________________________________"
git clone https://github.com/laramies/theHarvester
sleep 5
echo "______________________________________________"
echo "[+]Instando o ViSql..."
echo "______________________________________________"
./aptInstallViSql.sh  
sleep 5
echo "______________________________________________"
echo "[+]Instando o Sqlmap..."
echo "______________________________________________"
./aptInstallSqlmap.sh   
sleep 5
echo "______________________________________________"
echo "[+]Instalando Youtube-Downloader..."
echo "______________________________________________"
./aptInstallYoutube.sh 
sleep 5
echo "______________________________________________"
echo "[+]Instalando RouterSploit..."
echo "______________________________________________"
./aptInstallRouterSploit.sh 
sleep 5
echo "______________________________________________"
echo "[+]Instalando Metasploit Tech Z India RAPID7..."
echo "______________________________________________"
./metasploit@Techzindia.sh
sleep 5
echo "[+]Instalando o Wpscan"
apt install -y gcc git ruby ruby-dev libcurl4-openssl-dev make zlib1g-dev
git clone https://github.com/wpscanteam/wpscan
