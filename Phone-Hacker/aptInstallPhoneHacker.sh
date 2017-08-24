echo "##############################################"
echo " Phone Hacker RFS - Termux/GnuRoot"
echo "##############################################"
echo "______________________________________________"
echo "[+]Configurando o Termux..."
echo "______________________________________________"
apt update && apt -y upgrade  
termux-setup-storage 
pkg install ncurses-utils 
su -c chmod a+x -R . 
su -c chmod 777 -R . 
echo "______________________________________________"
echo "[+]Instando o Sudo..." 
echo "______________________________________________"
su -c cat sudo > /data/data/com.termux/files/usr/bin/sudo 
su -c chmod 777 /data/data/com.termux/files/usr/bin/sudo 
echo "______________________________________________"
echo "[+]Instando o Ngrok..."
echo "______________________________________________"
su -c cat ngrok > /data/data/com.termux/files/usr/bin/ngrok  
su -c chmod 777 /data/data/com.termux/files/usr/bin/ngrok  
echo "______________________________________________"
echo "[+]Instalando Apps && libs..."
echo "______________________________________________"
chmod a+x aptInstallApps.sh   
./aptInstallApps.sh    
echo "______________________________________________"
echo "[+]Instalando Python Libs..."
echo "______________________________________________"
./aptInstallPythonLibs.sh   
echo "______________________________________________"
echo "[+]Instando o The Harvester..."
echo "______________________________________________"
git clone https://github.com/laramies/theHarvester
echo "______________________________________________"
echo "[+]Instando o ViSql..."
echo "______________________________________________"
./aptInstallViSql.sh  
echo "______________________________________________"
echo "[+]Instando o Sqlmap..."
echo "______________________________________________"
./aptInstallSqlmap.sh   
echo "______________________________________________"
echo "[+]Instalando Youtube-Downloader..."
echo "______________________________________________"
./aptInstallYoutube.sh 
echo "______________________________________________"
echo "[+]Instalando o Scapy..."
echo "______________________________________________"
./aptInstallScapy.sh 
echo "______________________________________________"
echo "[+]Instalando Metasploit Tech Z India RAPID7..."
echo "______________________________________________"
./aptInstallMetasploit.sh 
echo "______________________________________________"
echo "[+]Configurando o PostgreSQL..."
echo "______________________________________________"
sudo sh initPstServer.sh 
sudo sh startServerPst.sh 
echo "______________________________________________"
echo "[+]Instalando RouterSploit..."
echo "______________________________________________"
./aptInstallRouterSploit.sh 
figlet Phone-Hacker-End
