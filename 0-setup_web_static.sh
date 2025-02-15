#!/usr/bin/env bash
# Install Nginx if it is not already installed
# Create necessary directories
# Create a fake HTML file for testing
# Create symbolic link
# Give ownership to ubuntu user and group
# Update Nginx configuration
# Restart Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo -e "server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default
service nginx restart
