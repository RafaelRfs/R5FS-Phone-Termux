echo "[+]Instalando binarios..."
su -c mv Client  /data/data/com.termux/files/usr/bin/
su -c mv Server /data/data/com.termux/files/usr/bin/
su -c mv mit  /data/data/com.termux/files/usr/bin/
su -c mv msfconsole /data/data/com.termux/files/usr/bin/
su -c mv network  /data/data/com.termux/files/usr/bin/
su -c mv network-nmap /data/data/com.termux/files/usr/bin/
su -c mv rsf /data/data/com.termux/files/usr/bin/
su -c mv showifi /data/data/com.termux/files/usr/bin/
su -c mv verser /data/data/com.termux/files/usr/bin/
su -c mv ShowDb /data/data/com.termux/files/usr/bin/
su -c mv ShowDbLocal /data/data/com.termux/files/usr/bin/
echo "[+]Binary permissions: "
su -c chmod 777 /data/data/com.termux/files/usr/bin/Client
su -c chmod 777 /data/data/com.termux/files/usr/bin/Server
su -c chmod 777 /data/data/com.termux/files/usr/bin/mit
su -c chmod 777 /data/data/com.termux/files/usr/bin/msfconsole
su -c chmod 777 /data/data/com.termux/files/usr/bin/network
su -c chmod 777 /data/data/com.termux/files/usr/bin/network-nmap
su -c chmod 777 /data/data/com.termux/files/usr/bin/rsf
su -c chmod 777 /data/data/com.termux/files/usr/bin/showifi
su -c chmod 777 /data/data/com.termux/files/usr/bin/verser
su -c chmod 777 /data/data/com.termux/files/usr/bin/ShowDb
su -c chmod 777 /data/data/com.termux/files/usr/bin/ShowDbLocal
