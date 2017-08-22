echo "______________________________________________"
echo "[+]Instalando o Fedora Linux..."
echo "______________________________________________"
sh aptInstalllFedora.sh
sleep 60

echo "______________________________________________"
echo "[+]Instalando o Wine..."
echo "______________________________________________"
startfedora
dnf install wine
sleep 60
