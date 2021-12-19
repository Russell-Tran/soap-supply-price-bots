# Run with sudo


# === For selenium_scripts ===
add-apt-repository ppa:deadsnakes/ppa   
apt-get update 
apt install python3.7
apt install pipenv
apt install firefox

# https://askubuntu.com/a/871077
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz -O /home/ubuntu/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf /home/ubuntu/geckodriver* -C /home/ubuntu/
chmod +x /home/ubuntu/geckodriver

# Make sure to add the following line to ~/.bashrc
# export PATH=$PATH:/home/ubuntu/
# Don't forget to `source .bashrc` if you want to have this modification take effect without logging out and back in to the instance.

# === For dispatch ===
apt install libnss3-tools