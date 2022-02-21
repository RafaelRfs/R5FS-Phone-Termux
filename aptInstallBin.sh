bin_dir=/data/data/com.termux/files/usr/bin/
echo "[+]Instalando binarios..."
su -c mv Client $bin_dir
su -c mv Server $bin_dir
su -c mv mit $bin_dir
su -c mv msfconsole $bin_dir
su -c mv network $bin_dir
su -c mv network-nmap $bin_dir
su -c mv rsf $bin_dir
su -c mv showifi $bin_dir
su -c mv verser $bin_dir
su -c mv ShowDb $bin_dir
su -c mv ShowDbLocal $bin_dir
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
