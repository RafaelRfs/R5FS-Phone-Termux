echo "______________________________________________"
echo "[+]Instalando o Fedora Linux..."
echo "______________________________________________"
./aptInstalllFedora.sh
echo "______________________________________________"
echo "[+]Instalando o Wine..."
echo "______________________________________________"
startfedora
dnf install wine
dnf install ettercap
dnf install iptables
dnf install sslstrip
