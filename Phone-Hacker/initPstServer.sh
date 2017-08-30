initdb pg
pg_ctl -D pg start
psql -d postgres -f user.sql
echo "[+]Configurando o Php Ini"
su -c mv php.ini /data/data/com.termux/files/usr/lib/php.ini
su -c chmod 777 /data/data/com.termux/files/usr/lib/php.ini
echo "[+]Configure o arquivo index-pdo.php, monte o server php e acesse o arquivo[index-pdo.php]"
