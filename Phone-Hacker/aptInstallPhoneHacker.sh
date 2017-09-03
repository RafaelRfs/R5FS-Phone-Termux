echo "##############################################"
echo " Phone Hacker R5FS ~> Termux/GnuRoot"
echo "##############################################"
echo "______________________________________________"
echo "[+]Configurando o Termux..."
echo "______________________________________________"
dir_bin=/data/data/com.termux/files/usr/bin/
apt update && apt -y upgrade  
termux-setup-storage 
pkg install ncurses-utils 
su -c chmod 777 *
sleep 5
echo "______________________________________________"
echo "[+]Instalando Apps && libs..."
echo "______________________________________________"
./aptInstallApps.sh
sleep 5
./aptInstallBin.sh
sleep 5
echo "______________________________________________"
echo "[+]Instalando Python Libs..."
echo "______________________________________________"
./aptInstallPythonLibs.sh   
sleep 5
echo "______________________________________________"
echo "[+]Instalando o Scapy..."
echo "______________________________________________"
./aptInstallScapy.sh 
sleep 5
echo "______________________________________________"
echo "[+]Configurando o PostgreSQL..."
echo "______________________________________________"
./initPstServer.sh 
./startServerPst.sh 
sleep 5
echo "______________________________________________"
echo "[+]Instando o Sudo..." 
echo "______________________________________________"
su -c mv sudo $dir_bin
su -c chmod 777 /data/data/com.termux/files/usr/bin/sudo
sleep 5
echo "______________________________________________"
echo "[+]Instando o Ngrok..."
echo "______________________________________________"
su -c mv ngrok $dir_bin
su -c chmod 777 /data/data/com.termux/files/usr/bin/ngrok
sleep 5
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
echo "______________________________________________"
echo "##############################################"
echo "[+]PHONE-HACKER Success"
echo "##############################################"
sleep 5
