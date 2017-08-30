initdb ~/pg
pgctl -D ~/pg start
psql -l
echo "[+]Configurando o Php Ini"
su -c cat php.ini > /data/data/com.termux/files/usr/lib/php.ini
su -c chmod 777 /data/data/com.termux/files/usr/lib/php.ini
