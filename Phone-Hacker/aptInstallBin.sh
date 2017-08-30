echo "[+]Instalando binarios..."
su -c cat Client > /data/data/com.termux/files/usr/bin/Client
su -c cat Server > /data/data/com.termux/files/usr/bin/Server
su -c cat mit > /data/data/com.termux/files/usr/bin/mit
su -c cat msfconsole > /data/data/com.termux/files/usr/bin/msfconsole
su -c cat network > /data/data/com.termux/files/usr/bin/network
su -c cat network-nmap > /data/data/com.termux/files/usr/bin/network-nmap
su -c cat rsf > /data/data/com.termux/files/usr/bin/rsf
su -c cat showifi > /data/data/com.termux/files/usr/bin/showifi

echo "[+]Binary permissions: "
su -c chmod 777 /data/data/com.termux/files/usr/bin/Client
su -c chmod 777 /data/data/com.termux/files/usr/bin/Server
su -c chmod 777 /data/data/com.termux/files/usr/bin/mit
su -c chmod 777 /data/data/com.termux/files/usr/bin/msfconsole
su -c chmod 777 /data/data/com.termux/files/usr/bin/network
su -c chmod 777 /data/data/com.termux/files/usr/bin/network-nmap
su -c chmod 777 /data/data/com.termux/files/usr/bin/rsf
su -c chmod 777 /data/data/com.termux/files/usr/bin/showifi
