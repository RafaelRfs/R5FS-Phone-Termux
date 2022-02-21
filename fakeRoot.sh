echo "this script emulates a fake root to use aplications with phone without root"
apt install proot
echo "proot -0" > ~/../usr/bin/sudo
chmod 777 ~/../usr/bin/sudo

sudo
