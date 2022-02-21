echo "______________________________________________"
echo "[+]Installing the Sudo..." 
echo "______________________________________________"
su -c cat sudo > /data/data/com.termux/files/usr/bin/sudo
su -c chmod 777 /data/data/com.termux/files/usr/bin/sudo
sleep 5
echo "______________________________________________"
echo "[+]Installing the Ngrok..."
echo "______________________________________________"
su -c cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
su -c chmod 777 /data/data/com.termux/files/usr/bin/ngrok
echo "______________________________________________"
