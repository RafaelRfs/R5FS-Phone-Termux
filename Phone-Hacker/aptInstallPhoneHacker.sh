echo "##############################################"
echo " Phone Hacker RFS - Termux/GnuRoot"
echo "##############################################"

echo "______________________________________________"
echo "[+]Configurando o Termux..."
echo "______________________________________________"
apt update && apt -y upgrade
termux-setup-storage
pkg install ncurses-utils

echo "______________________________________________"
echo "[+]Instando o Sudo..."
echo "______________________________________________"
su -test cat sudo > /data/data/com.termux/files/usr/bin/sudo
su -test chmod 700 /data/data/com.termux/files/usr/bin/sudo

echo "______________________________________________"
echo "[+]Instando o Ngrok..."
echo "______________________________________________"
sudo chmod 777 ngrok
sudo cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
sudo chmod 777 /data/data/com.termux/files/usr/bin/ngrok

echo "______________________________________________"
echo "[+]Instando o ViSql..."
echo "______________________________________________"
sh aptInstallViSql.sh

echo "______________________________________________"
echo "[+]Instando o Sqlmap..."
echo "______________________________________________"
sh aptInstallSqlmap

echo "______________________________________________"
echo "[+]Instalando Apps && libs..."
echo "______________________________________________"
sh aptInstallApps.sh

echo "______________________________________________"
echo "[+]Instalando Youtube-Downloader..."
echo "______________________________________________"
sh aptInstallYoutube.sh

echo "______________________________________________"
echo "[+]Instalando o Scapy..."
echo "______________________________________________"
sh aptInstallScapy.sh

echo "______________________________________________"
echo "[+]Instalando Metasploit Tech Z India RAPID7..."
echo "______________________________________________"
sh aptInstallMetasploit.sh
cd ~

echo "______________________________________________"
echo "[+]Configurando o PostgreSQL..."
echo "______________________________________________"
sudo sh initPstServer.sh
sudo sh startServerPst.sh

cd ~
echo "______________________________________________"
echo "[+]Instalando RouterSploit..."
echo "______________________________________________"
sh aptInstallRouterSploit.sh
cd ~

