#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# update & upgrade
sudo apt-get -y update
sudo apt-get -y upgrade

# install nginx
sudo apt-get -y install nginx

# create directories
# /data/web_static/shared/
# /data/web_static/releases/
# /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create /data/web_static/releases/test/index.html containing tests for Nginx configration
echo "" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ to ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# update Nginx config to serve /data/web_static/current/ to hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx start
