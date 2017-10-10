su -c dos2unix *.sh
su -c chmod 777 -R *
./aptInstallPhoneHacker.sh
echo "[+]Installing Programs..."
./aptInstallPrograms.sh
echo "[+]Installing Kali..."
./aptInstallKali.sh
echo "[+]Installing Fedora..."
./aptInstalllFedora.sh
