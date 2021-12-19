add-apt-repository ppa:deadsnakes/ppa   
apt-get update 
apt install python3.7
apt install pipenv

# https://askubuntu.com/a/871077
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
#export PATH=$PATH:/path-to-extracted-file/.