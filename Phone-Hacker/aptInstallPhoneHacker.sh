echo "##############################################"
echo " Phone Hacker RFS - Termux/GnuRoot"
echo "##############################################"

echo "______________________________________________"
echo "[+]Configurando o Termux..."
echo "______________________________________________"
apt update && apt -y upgrade
termux-setup-storage
pkg install ncurses-utils
sleep 60

echo "______________________________________________"
echo "[+]Instando o Sudo..."
echo "______________________________________________"
su -c cat sudo > /data/data/com.termux/files/usr/bin/sudo
su -c chmod 700 /data/data/com.termux/files/usr/bin/sudo
sleep 60

echo "______________________________________________"
echo "[+]Instando o Ngrok..."
echo "______________________________________________"
sudo chmod 777 ngrok
sudo cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
sudo chmod 777 /data/data/com.termux/files/usr/bin/ngrok
sleep 60

echo "______________________________________________"
echo "[+]Instalando Apps && libs..."
echo "______________________________________________"
sh aptInstallApps.sh
sleep 60

echo "______________________________________________"
echo "[+]Instando o The Harvester..."
echo "______________________________________________"
git clone https://github.com/laramies/theHarvester

sleep 60
echo "______________________________________________"
echo "[+]Instando o ViSql..."
echo "______________________________________________"
sh aptInstallViSql.sh
sleep 60

echo "______________________________________________"
echo "[+]Instando o Sqlmap..."
echo "______________________________________________"
sh aptInstallSqlmap
sleep 60

echo "______________________________________________"
echo "[+]Instalando Youtube-Downloader..."
echo "______________________________________________"
sh aptInstallYoutube.sh
sleep 60

echo "______________________________________________"
echo "[+]Instalando o Scapy..."
echo "______________________________________________"
sh aptInstallScapy.sh
sleep 60

echo "______________________________________________"
echo "[+]Instalando Metasploit Tech Z India RAPID7..."
echo "______________________________________________"
sh aptInstallMetasploit.sh
cd $HOME
sleep 60

echo "______________________________________________"
echo "[+]Configurando o PostgreSQL..."
echo "______________________________________________"
sudo sh initPstServer.sh
sudo sh startServerPst.sh
sleep 60

cd $HOME
echo "______________________________________________"
echo "[+]Instalando RouterSploit..."
echo "______________________________________________"
sh aptInstallRouterSploit.sh
cd $HOME
sleep 60
figlet Phone-Hacker-End
