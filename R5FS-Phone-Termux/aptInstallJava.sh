apt install wget
cd ~
wget https://raw.githubusercontent.com/Hax4us/java/master/installjava > installjava.sh
dos2unix installjava.sh

sh installjava.sh

apt install proot

echo "proot -0" > ~/../usr/bin/sudo


chmod 777  ~/../usr/bin/sudo


