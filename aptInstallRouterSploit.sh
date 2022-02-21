echo "[+++]Routersploit in your system..."
apt install python-dev python-pip libncurses5-dev git
git clone https://github.com/reverse-shell/routersploit
cd routersploit
pip install -r requirements.txt
cd ..
