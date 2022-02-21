initdb pg
pg_ctl -D pg start
psql -d postgres -f user.sql
echo "[+]Configurando o Php Ini"
su -c mv php.ini /data/data/com.termux/files/usr/lib/
su -c chmod 777 /data/data/com.termux/files/usr/lib/php.ini
echo "[+]SERVER PSGSQL + PHP 7 INSTALL COMPLETE..."
