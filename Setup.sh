su -c dos2unix *.sh
su -c chmod 777 -R *
apt install tsu
tsu
./aptInstallPhoneHacker.sh
echo "[+]Installing Programs..."
./aptInstallPrograms.sh
echo "[+]Installing Kali..."
./aptInstallKali.sh

chmod 777 Kali
su -c mv Kali /data/data/com.termux/files/usr/bin

echo "[+]Installing Fedora..."
./aptInstalllFedora.sh
