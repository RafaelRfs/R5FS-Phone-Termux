apt update && apt -y upgrade
pkg install ncurses-utils
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
sh aptInstall.sh
sh aptInstallMetasploit.sh